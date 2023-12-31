common/bounded-executor/src/lib.rs
==================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! A bounded tokio [`TaskExecutor`]. Only a bounded number of tasks can run
//! concurrently when spawned through this executor, defined by the initial
//! `capacity`.

use futures::future::{Future, FutureExt, TryFutureExt};
use solana_libra_futures_semaphore::Semaphore;
use tokio::runtime::TaskExecutor;

#[derive(Clone, Debug)]
pub struct BoundedExecutor {
    semaphore: Semaphore,
    executor: TaskExecutor,
}

/// Returned by [`BoundedExecutor::try_spawn`] if it is at capacity.
pub enum SpawnError {
    AtCapacity,
}

impl BoundedExecutor {
    /// Create a new `BoundedExecutor` from an existing tokio [`TaskExecutor`]
    /// with a maximum concurrent task capacity of `capacity`.
    pub fn new(capacity: usize, executor: TaskExecutor) -> Self {
        let semaphore = Semaphore::new(capacity);
        Self {
            semaphore,
            executor,
        }
    }

    /// Spawn a [`Future`] on the `BoundedExecutor`. This function is async and
    /// will block if the executor is at capacity.
    pub async fn spawn<F>(&self, f: F)
    where
        F: Future<Output = ()> + Send + 'static,
    {
        let spawn_permit = self.semaphore.acquire().await;
        let f = f.map(move |_| drop(spawn_permit));
        self.executor.spawn(f.boxed().unit_error().compat());
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use futures::{compat::Future01CompatExt, executor::block_on, future::Future};
    use std::{
        sync::atomic::{AtomicU32, Ordering},
        time::{Duration, Instant},
    };
    use tokio::{runtime::Runtime, timer::Delay};

    fn yield_task() -> impl Future<Output = ()> {
        Delay::new(Instant::now() + Duration::from_millis(1))
            .compat()
            .map(|_| ())
    }

    // spawn NUM_TASKS futures on a BoundedExecutor, ensuring that no more than
    // MAX_WORKERS ever enter the critical section.
    #[test]
    fn concurrent_bounded_executor() {
        const MAX_WORKERS: u32 = 20;
        const NUM_TASKS: u32 = 1000;
        static WORKERS: AtomicU32 = AtomicU32::new(0);
        static COMPLETED_TASKS: AtomicU32 = AtomicU32::new(0);

        let rt = Runtime::new().unwrap();
        let executor = rt.executor();
        let executor = BoundedExecutor::new(MAX_WORKERS as usize, executor);

        for _ in 0..NUM_TASKS {
            block_on(executor.spawn(async move {
                // acquired permit, there should only ever be MAX_WORKERS in this
                // critical section

                let prev_workers = WORKERS.fetch_add(1, Ordering::SeqCst);
                assert!(prev_workers < MAX_WORKERS);

                // yield back to the tokio scheduler
                yield_task().await;

                let prev_workers = WORKERS.fetch_sub(1, Ordering::SeqCst);
                assert!(prev_workers > 0 && prev_workers <= MAX_WORKERS);

                COMPLETED_TASKS.fetch_add(1, Ordering::Relaxed);
            }));
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


