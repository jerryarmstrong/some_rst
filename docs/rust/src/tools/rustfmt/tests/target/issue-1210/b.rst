src/tools/rustfmt/tests/target/issue-1210/b.rs
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
            None => panic!(
                "\ntarget `{}`: is not, \
                 configured as a host,
                            only as a target\n\n",
                target
            ),
        }
    }
}


