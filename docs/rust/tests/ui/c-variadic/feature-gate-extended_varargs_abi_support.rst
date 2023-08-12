tests/ui/c-variadic/feature-gate-extended_varargs_abi_support.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn efiapi(f: extern "efiapi" fn(usize, ...)) {
    //~^ ERROR: C-variadic function must have a compatible calling convention, like `C` or `cdecl`
    //~^^ ERROR: using calling conventions other than `C` or `cdecl` for varargs functions is unstable
    f(22, 44);
}
fn sysv(f: extern "sysv64" fn(usize, ...)) {
    //~^ ERROR: C-variadic function must have a compatible calling convention, like `C` or `cdecl`
    //~^^ ERROR: using calling conventions other than `C` or `cdecl` for varargs functions is unstable
    f(22, 44);
}
fn win(f: extern "win64" fn(usize, ...)) {
    //~^ ERROR: C-variadic function must have a compatible calling convention, like `C` or `cdecl`
    //~^^ ERROR: using calling conventions other than `C` or `cdecl` for varargs functions is unstable
    f(22, 44);
}

fn main() {}


