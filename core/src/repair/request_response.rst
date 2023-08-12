core/src/repair/request_response.rs
===================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    pub trait RequestResponse {
    type Response;
    fn num_expected_responses(&self) -> u32;
    fn verify_response(&self, response: &Self::Response) -> bool;
}


