tests/ui/cfg/expanded-cfg.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! mac {
    {} => {
        #[cfg(attr)]
        mod m {
            #[lang_item]
            fn f() {}

            #[cfg_attr(target_thread_local, custom)]
            fn g() {}
        }

        #[cfg(attr)]
        unconfigured_invocation!();
    }
}

mac! {}

fn main() {}


