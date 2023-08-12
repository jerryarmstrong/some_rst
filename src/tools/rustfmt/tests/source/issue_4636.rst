src/tools/rustfmt/tests/source/issue_4636.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait PrettyPrinter<'tcx>:
    Printer<
        'tcx,
        Error = fmt::Error,
        Path = Self,
        Region = Self,
        Type = Self,
        DynExistential = Self,
        Const = Self,
    > + fmt::Write
    {
         //
    }

