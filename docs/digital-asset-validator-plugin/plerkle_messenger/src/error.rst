plerkle_messenger/src/error.rs
==============================

Last edited: 2023-08-03 21:06:53

Contents:

.. code-block:: rs

    use thiserror::Error;

#[derive(Error, Debug)]
pub enum MessengerError {
    #[error("Missing or invalid configuration: ({msg})")]
    ConfigurationError { msg: String },

    #[error("Error creating connection: ({msg})")]
    ConnectionError { msg: String },

    #[error("Error sending data: ({msg})")]
    SendError { msg: String },

    #[error("Error receiving data: ({msg})")]
    ReceiveError { msg: String },

    #[error("Error ACKing message: ({msg})")]
    AckError { msg: String },

    #[error("Error autoclaiming message: ({msg})")]
    AutoclaimError { msg: String },
}


