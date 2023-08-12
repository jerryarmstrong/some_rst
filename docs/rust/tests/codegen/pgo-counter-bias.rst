tests/codegen/pgo-counter-bias.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that __llvm_profile_counter_bias does not get internalized by lto.

// ignore-macos -runtime-counter-relocation not honored on Mach-O
// compile-flags: -Cprofile-generate -Cllvm-args=-runtime-counter-relocation -Clto=fat
// needs-profiler-support
// no-prefer-dynamic

// CHECK: @__llvm_profile_counter_bias = {{.*}}global

pub fn main() {}


