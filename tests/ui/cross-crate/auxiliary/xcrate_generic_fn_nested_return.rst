tests/ui/cross-crate/auxiliary/xcrate_generic_fn_nested_return.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Request {
    pub id: String,
    pub arg: String,
}

pub fn decode<T>() -> Result<Request, ()> {
    (|| {
        Ok(Request {
            id: "hi".to_owned(),
            arg: match Err(()) {
                Ok(v) => v,
                Err(e) => return Err(e)
            },
        })
    })()
}


