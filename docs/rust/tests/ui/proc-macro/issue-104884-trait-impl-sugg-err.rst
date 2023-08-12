tests/ui/proc-macro/issue-104884-trait-impl-sugg-err.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:issue-104884.rs

use std::collections::BinaryHeap;

#[macro_use]
extern crate issue_104884;

#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct PriorityQueueEntry<T> {
    value: T,
}

#[derive(PartialOrd, AddImpl)]
//~^ ERROR can't compare `PriorityQueue<T>` with `PriorityQueue<T>`
//~| ERROR the trait bound `PriorityQueue<T>: Eq` is not satisfied
//~| ERROR can't compare `T` with `T`

struct PriorityQueue<T>(BinaryHeap<PriorityQueueEntry<T>>);

fn main() {}


