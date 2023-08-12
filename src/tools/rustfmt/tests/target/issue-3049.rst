src/tools/rustfmt/tests/target/issue-3049.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual
fn main() {
    something.aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .bench_function(|| {
                 let x = hello();
             });

    something.aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .bench_function(arg, || {
                 let x = hello();
             });

    something.aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .aaaaaaaaaaaa()
             .bench_function(arg,
                             || {
                                 let x = hello();
                             },
                             arg);

    AAAAAAAAAAA.function(|| {
                   let _ = ();
               });

    AAAAAAAAAAA.chain().function(|| {
                           let _ = ();
                       })
}


