library/profiler_builtins/src/lib.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
#![feature(profiler_runtime)]
#![profiler_runtime]
#![unstable(
    feature = "profiler_runtime_lib",
    reason = "internal implementation detail of rustc right now",
    issue = "none"
)]
#![allow(unused_features)]
#![feature(staged_api)]


