common/futures-semaphore/src/lib.rs
===================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! `Semaphore` holds a set of permits. Permits are used to synchronize access
//! to a shared resource. Before accessing the shared resource, callers must
//! acquire a permit from the semaphore. Once the permit is acquired, the caller
//! then enters the critical section. When the caller is finished, they drop the
//! permit to release it back to the semaphore.
//!
//! `Semaphore` is futures-aware. Acquiring a [`Permit`] is an async function,
//! which will yield to the futures executor if no permits are available and be
//! woken up when one becomes available.
//!
//! In contrast, acquiring a permit from a [`std::sync::Mutex`] +
//! [`std::sync::Condvar`] style semaphore will block the entire OS thread, which
//! could potentially deadlock the futures runtime if enough tasks are waiting on
//! the semaphore.

use futures01::{future::Future as Future01, Async as Async01, Poll as Poll01};
use futures03::compat::Future01CompatExt;
use std::sync::Arc;
use tokio_sync::semaphore::{AcquireError, Permit as TokioPermit, Semaphore as TokioSemaphore};

/// The wrapped tokio_sync [`Semaphore`](TokioSemaphore) and total permit capacity.
#[derive(Debug)]
struct Inner {
    semaphore: TokioSemaphore,
    capacity: usize,
}

/// A futures-aware semaphore.
#[derive(Clone, Debug)]
pub struct Semaphore {
    inner: Arc<Inner>,
}

/// A permit acquired from a semaphore, allowing access to a shared resource.
/// Dropping a `Permit` will release it back to the semaphore.
#[derive(Debug)]
pub struct Permit {
    inner: Arc<Inner>,
    permit: TokioPermit,
}

impl Semaphore {
    /// Create a new semaphore with `capacity` number of available permits.
    pub fn new(capacity: usize) -> Self {
        Self {
            inner: Arc::new(Inner {
                semaphore: TokioSemaphore::new(capacity),
                capacity,
            }),
        }
    }

    pub fn capacity(&self) -> usize {
        self.inner.capacity
    }

    pub fn available_permits(&self) -> usize {
        self.inner.semaphore.available_permits()
    }

    pub fn is_idle(&self) -> bool {
        self.available_permits() == self.capacity()
    }

    pub fn is_full(&self) -> bool {
        self.available_permits() == 0
    }

    /// Acquire an available permit from the semaphore, blocking until none are
    /// available.
    pub async fn acquire(&self) -> Permit {
        let permit = Permit {
            inner: Arc::clone(&self.inner),
            permit: TokioPermit::new(),
        };

        PermitFuture01::new(permit)
            .compat()
            .await
            // The TokioSemaphore is not dropped yet and our wrapper never calls
            // .close(), so the TokioSemaphore can never be closed unless all
            // references, including this &self, have been dropped.
            .expect("TokioSemaphore is never closed")
    }

    /// Try to acquire an available permit from the semaphore. If no permits are
    /// available, return `None`.
    pub fn try_acquire(&self) -> Option<Permit> {
        let mut permit = TokioPermit::new();
        match permit.try_acquire(&self.inner.semaphore) {
            Ok(()) => Some(Permit {
                inner: Arc::clone(&self.inner),
                permit,
            }),
            Err(err) => {
                // The TokioSemaphore is not dropped yet and our wrapper never
                // calls .close(), so the TokioSemaphore can never be closed
                // unless all references, including this &self, have been
                // dropped.
                assert!(!err.is_closed());
                assert!(err.is_no_permits());
                None
            }
        }
    }
}

impl Permit {
    fn release(&mut self) {
        self.permit.release(&self.inner.semaphore);
    }
}

impl Drop for Permit {
    fn drop(&mut self) {
        self.release();
    }
}

struct PermitFuture01 {
    permit: Option<Permit>,
}

impl PermitFuture01 {
    fn new(permit: Permit) -> Self {
        Self {
            permit: Some(permit),
        }
    }
}

impl Future01 for PermitFuture01 {
    type Item = Permit;
    type Error = AcquireError;

    fn poll(&mut self) -> Poll01<Self::Item, Self::Error> {
        let mut permit = self.permit.take().unwrap();

        match permit.permit.poll_acquire(&permit.inner.semaphore) {
            Ok(Async01::Ready(())) => Ok(Async01::Ready(permit)),
            Ok(Async01::NotReady) => {
                self.permit = Some(permit);
                Ok(Async01::NotReady)
            }
            Err(e) => Err(e),
        }
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use futures03::{
        executor::block_on,
        future::{Future, FutureExt, TryFutureExt},
    };
    use std::{
        sync::atomic::{AtomicU32, Ordering},
        time::{Duration, Instant},
    };
    use tokio::{runtime::Runtime, timer::Delay};

    #[test]
    fn basic_functionality_semaphore() {
        let s = Semaphore::new(3);

        assert!(s.is_idle());

        let _p1 = block_on(s.acquire());
        let p2 = block_on(s.acquire());
        let p3 = block_on(s.acquire());

        assert!(s.is_full());
        assert!(s.try_acquire().is_none());

        drop(p2);

        assert!(!s.is_full());
        assert!(!s.is_idle());

        let _p4 = block_on(s.acquire());

        assert!(s.is_full());
        assert!(s.try_acquire().is_none());

        drop(p3);

        assert!(!s.is_full());
        assert!(!s.is_idle());

        assert!(s.try_acquire().is_some());
    }

    fn yield_task() -> impl Future<Output = ()> {
        Delay::new(Instant::now() + Duration::from_millis(1))
            .compat()
            .map(|_| ())
    }

    // spawn NUM_TASKS futures that acquire a common semaphore, ensuring that no
    // more than MAX_WORKERS ever enter the critical section.
    #[test]
    fn concurrent_semaphore() {
        const MAX_WORKERS: u32 = 20;
        const NUM_TASKS: u32 = 1000;
        static WORKERS: AtomicU32 = AtomicU32::new(0);
        static COMPLETED_TASKS: AtomicU32 = AtomicU32::new(0);
        let semaphore = Semaphore::new(MAX_WORKERS as usize);

        let mut rt = Runtime::new().unwrap();

        for _ in 0..NUM_TASKS {
            let semaphore = semaphore.clone();
            let f = async move {
                let _permit = semaphore.acquire().await;

                // acquired permit, there should only ever be MAX_WORKERS in this
                // critical section

                let prev_workers = WORKERS.fetch_add(1, Ordering::SeqCst);
                assert!(prev_workers < MAX_WORKERS);

                // yield back to the tokio scheduler
                yield_task().await;

                let prev_workers = WORKERS.fetch_sub(1, Ordering::SeqCst);
                assert!(prev_workers > 0 && prev_workers <= MAX_WORKERS);

                COMPLETED_TASKS.fetch_add(1, Ordering::Relaxed);

                // drop _permit and release access
            };
            rt.spawn(f.boxed().unit_error().compat());
        }

        // spin until completed
        loop {
            let completed = COMPLETED_TASKS.load(Ordering::Relaxed);
            if completed == NUM_TASKS {
                break;
            } else {
                ::std::sync::atomic::spin_loop_hint();
            }
        }
    }
}


