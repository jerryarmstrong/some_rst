src/tools/rustfmt/tests/target/string-lit-custom.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let expected = "; ModuleID = \'foo\'

; Function Attrs: nounwind
declare void @llvm.memset.p0i8.i32(i8* nocapture, i8, i32, i32, i1) #0

declare i32 @write(i32, i8*, i32)

declare i32 @putchar(i32)

declare i32 @getchar()

define i32 @main() {
entry:
  ret i32 0
}

attributes #0 = { nounwind }
";
}


