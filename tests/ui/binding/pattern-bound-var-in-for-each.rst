tests/ui/binding/pattern-bound-var-in-for-each.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests that codegen_path checks whether a
// pattern-bound var is an upvar (when codegenning
// the for-each body)


fn foo(src: usize) {

    match Some(src) {
      Some(src_id) => {
        for _i in 0_usize..10_usize {
            let yyy = src_id;
            assert_eq!(yyy, 0_usize);
        }
      }
      _ => { }
    }
}

pub fn main() { foo(0_usize); }


