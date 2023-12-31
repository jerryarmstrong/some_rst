crates/core_arch/src/wasm32/memory.rs
=====================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    #[cfg(test)]
use stdsimd_test::assert_instr;
#[cfg(test)]
use wasm_bindgen_test::wasm_bindgen_test;

extern "C" {
    #[link_name = "llvm.wasm.memory.grow.i32"]
    fn llvm_memory_grow(mem: i32, pages: i32) -> i32;
    #[link_name = "llvm.wasm.memory.size.i32"]
    fn llvm_memory_size(mem: i32) -> i32;
}

/// Corresponding intrinsic to wasm's [`memory.size` instruction][instr]
///
/// This function, when called, will return the current memory size in units of
/// pages. The current WebAssembly page size is 65536 bytes (64 KB).
///
/// The argument `mem` is the numerical index of which memory to return the
/// size of. Note that currently the WebAssembly specification only supports one
/// memory, so it is required that zero is passed in. The argument is present to
/// be forward-compatible with future WebAssembly revisions. If a nonzero
/// argument is passed to this function it will currently unconditionally abort.
///
/// [instr]: http://webassembly.github.io/spec/core/exec/instructions.html#exec-memory-size
#[inline]
#[cfg_attr(test, assert_instr("memory.size", mem = 0))]
#[rustc_args_required_const(0)]
#[stable(feature = "simd_wasm32", since = "1.33.0")]
pub fn memory_size(mem: u32) -> usize {
    unsafe {
        if mem != 0 {
            crate::intrinsics::abort();
        }
        llvm_memory_size(0) as usize
    }
}

/// Corresponding intrinsic to wasm's [`memory.grow` instruction][instr]
///
/// This function, when called, will attempt to grow the default linear memory
/// by the specified `delta` of pages. The current WebAssembly page size is
/// 65536 bytes (64 KB). If memory is successfully grown then the previous size
/// of memory, in pages, is returned. If memory cannot be grown then
/// `usize::max_value()` is returned.
///
/// The argument `mem` is the numerical index of which memory to return the
/// size of. Note that currently the WebAssembly specification only supports one
/// memory, so it is required that zero is passed in. The argument is present to
/// be forward-compatible with future WebAssembly revisions. If a nonzero
/// argument is passed to this function it will currently unconditionally abort.
///
/// [instr]: http://webassembly.github.io/spec/core/exec/instructions.html#exec-memory-grow
#[inline]
#[cfg_attr(test, assert_instr("memory.grow", mem = 0))]
#[rustc_args_required_const(0)]
#[stable(feature = "simd_wasm32", since = "1.33.0")]
pub fn memory_grow(mem: u32, delta: usize) -> usize {
    unsafe {
        if mem != 0 {
            crate::intrinsics::abort();
        }
        llvm_memory_grow(0, delta as i32) as isize as usize
    }
}


