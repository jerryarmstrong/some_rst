README.md
=========

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: md

    # Fork of the Rust Programming Language's stdsimd library

Used by [rust-bpf-sysroot](https://github.com/solana-labs/rust-bpf-sysroot) and contains submodules, to sync use:

```git clone --recurse-submodules ```

---

stdsimd - Rust's standard library SIMD components
=======

[![Travis-CI Status]][travis] [![Appveyor Status]][appveyor] 

# Crates

This repository contains two main crates:

* [![core_arch_crate_badge]][core_arch_crate_link]
  [![core_arch_docs_badge]][core_arch_docs_link]
  [`core_arch`](crates/core_arch/README.md) implements `core::arch` - Rust's
  core library architecture-specific intrinsics, and
  
* [![std_detect_crate_badge]][std_detect_crate_link]
  [![std_detect_docs_badge]][std_detect_docs_link]
  [`std_detect`](crates/std_detect/README.md) implements `std::detect` - Rust's
  standard library run-time CPU feature detection.

The `std::simd` component now lives in the
[`packed_simd`](https://github.com/rust-lang-nursery/packed_simd) crate.

# How to do a release

To do a release of the `core_arch` and `std_detect` crates, 

* bump up the version appropriately,
* comment out the `dev-dependencies` in their `Cargo.toml` files (due to
  https://github.com/rust-lang/cargo/issues/4242),
* publish the crates.

[travis]: https://travis-ci.com/rust-lang-nursery/stdsimd
[Travis-CI Status]: https://travis-ci.com/rust-lang-nursery/stdsimd.svg?branch=master
[appveyor]: https://ci.appveyor.com/project/rust-lang-libs/stdsimd/branch/master
[Appveyor Status]: https://ci.appveyor.com/api/projects/status/ix74qhmilpibn00x/branch/master?svg=true
[core_arch_crate_badge]: https://img.shields.io/crates/v/core_arch.svg
[core_arch_crate_link]: https://crates.io/crates/core_arch
[core_arch_docs_badge]: https://docs.rs/core_arch/badge.svg
[core_arch_docs_link]: https://docs.rs/core_arch/
[std_detect_crate_badge]: https://img.shields.io/crates/v/std_detect.svg
[std_detect_crate_link]: https://crates.io/crates/std_detect
[std_detect_docs_badge]: https://docs.rs/std_detect/badge.svg
[std_detect_docs_link]: https://docs.rs/std_detect/


