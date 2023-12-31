src/alloc/src/collections/vec_deque/iter_mut.rs
===============================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use core::fmt;
use core::iter::FusedIterator;
use core::marker::PhantomData;

use super::{count, wrap_index, RingSlices};

/// A mutable iterator over the elements of a `VecDeque`.
///
/// This `struct` is created by the [`iter_mut`] method on [`super::VecDeque`]. See its
/// documentation for more.
///
/// [`iter_mut`]: super::VecDeque::iter_mut
#[stable(feature = "rust1", since = "1.0.0")]
pub struct IterMut<'a, T: 'a> {
    // Internal safety invariant: the entire slice is dereferencable.
    pub(crate) ring: *mut [T],
    pub(crate) tail: usize,
    pub(crate) head: usize,
    pub(crate) phantom: PhantomData<&'a mut [T]>,
}

// SAFETY: we do nothing thread-local and there is no interior mutability,
// so the usual structural `Send`/`Sync` apply.
#[stable(feature = "rust1", since = "1.0.0")]
unsafe impl<T: Send> Send for IterMut<'_, T> {}
#[stable(feature = "rust1", since = "1.0.0")]
unsafe impl<T: Sync> Sync for IterMut<'_, T> {}

#[stable(feature = "collection_debug", since = "1.17.0")]
impl<T: fmt::Debug> fmt::Debug for IterMut<'_, T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let (front, back) = RingSlices::ring_slices(self.ring, self.head, self.tail);
        // SAFETY: these are the elements we have not handed out yet, so aliasing is fine.
        // The `IterMut` invariant also ensures everything is dereferencable.
        let (front, back) = unsafe { (&*front, &*back) };
        f.debug_tuple("IterMut").field(&front).field(&back).finish()
    }
}

#[stable(feature = "rust1", since = "1.0.0")]
impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;

    #[inline]
    fn next(&mut self) -> Option<&'a mut T> {
        if self.tail == self.head {
            return None;
        }
        let tail = self.tail;
        self.tail = wrap_index(self.tail.wrapping_add(1), self.ring.len());

        unsafe {
            let elem = self.ring.get_unchecked_mut(tail);
            Some(&mut *elem)
        }
    }

    #[inline]
    fn size_hint(&self) -> (usize, Option<usize>) {
        let len = count(self.tail, self.head, self.ring.len());
        (len, Some(len))
    }

    fn fold<Acc, F>(self, mut accum: Acc, mut f: F) -> Acc
    where
        F: FnMut(Acc, Self::Item) -> Acc,
    {
        let (front, back) = RingSlices::ring_slices(self.ring, self.head, self.tail);
        // SAFETY: these are the elements we have not handed out yet, so aliasing is fine.
        // The `IterMut` invariant also ensures everything is dereferencable.
        let (front, back) = unsafe { (&mut *front, &mut *back) };
        accum = front.iter_mut().fold(accum, &mut f);
        back.iter_mut().fold(accum, &mut f)
    }

    fn nth(&mut self, n: usize) -> Option<Self::Item> {
        if n >= count(self.tail, self.head, self.ring.len()) {
            self.tail = self.head;
            None
        } else {
            self.tail = wrap_index(self.tail.wrapping_add(n), self.ring.len());
            self.next()
        }
    }

    #[inline]
    fn last(mut self) -> Option<&'a mut T> {
        self.next_back()
    }
}

#[stable(feature = "rust1", since = "1.0.0")]
impl<'a, T> DoubleEndedIterator for IterMut<'a, T> {
    #[inline]
    fn next_back(&mut self) -> Option<&'a mut T> {
        if self.tail == self.head {
            return None;
        }
        self.head = wrap_index(self.head.wrapping_sub(1), self.ring.len());

        unsafe {
            let elem = self.ring.get_unchecked_mut(self.head);
            Some(&mut *elem)
        }
    }

    fn rfold<Acc, F>(self, mut accum: Acc, mut f: F) -> Acc
    where
        F: FnMut(Acc, Self::Item) -> Acc,
    {
        let (front, back) = RingSlices::ring_slices(self.ring, self.head, self.tail);
        // SAFETY: these are the elements we have not handed out yet, so aliasing is fine.
        // The `IterMut` invariant also ensures everything is dereferencable.
        let (front, back) = unsafe { (&mut *front, &mut *back) };
        accum = back.iter_mut().rfold(accum, &mut f);
        front.iter_mut().rfold(accum, &mut f)
    }
}

#[stable(feature = "rust1", since = "1.0.0")]
impl<T> ExactSizeIterator for IterMut<'_, T> {
    fn is_empty(&self) -> bool {
        self.head == self.tail
    }
}

#[stable(feature = "fused", since = "1.26.0")]
impl<T> FusedIterator for IterMut<'_, T> {}


