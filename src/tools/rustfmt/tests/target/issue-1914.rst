src/tools/rustfmt/tests/target/issue-1914.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-max_width: 80

extern "C" {
    #[link_name = "_ZN7MyClass26example_check_no_collisionE"]
    pub static mut MyClass_example_check_no_collision:
        *const ::std::os::raw::c_int;
}


