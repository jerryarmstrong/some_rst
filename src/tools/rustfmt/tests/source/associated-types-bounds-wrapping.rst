src/tools/rustfmt/tests/source/associated-types-bounds-wrapping.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test proper wrapping of long associated type bounds

pub trait HttpService {
    type WsService: 'static + Service<Request = WsCommand, Response = WsResponse, Error = ServerError>;
}


