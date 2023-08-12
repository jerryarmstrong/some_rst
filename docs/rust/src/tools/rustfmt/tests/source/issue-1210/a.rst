src/tools/rustfmt/tests/source/issue-1210/a.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: true
// rustfmt-max_width: 50

impl Foo {
    fn cxx(&self, target: &str) -> &Path {
        match self.cxx.get(target) {
            Some(p) => p.path(),
            None => panic!("\n\ntarget `{}` is not configured as a host,
                            only as a target\n\n", target),
        }
    }
}


