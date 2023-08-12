src/tools/rustfmt/tests/target/pub-restricted.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub(super) enum WriteState<D> {
    WriteId {
        id: U64Writer,
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteSize {
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteData(Writer<D>),
}

pub(crate) enum WriteState<D> {
    WriteId {
        id: U64Writer,
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteSize {
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteData(Writer<D>),
}

pub(in global::path::to::some_mod) enum WriteState<D> {
    WriteId {
        id: U64Writer,
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteSize {
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteData(Writer<D>),
}

pub(in local::path::to::some_mod) enum WriteState<D> {
    WriteId {
        id: U64Writer,
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteSize {
        size: U64Writer,
        payload: Option<Writer<D>>,
    },
    WriteData(Writer<D>),
}


