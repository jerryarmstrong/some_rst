src/config/errors.rs
====================

Last edited: 2023-08-11 21:59:14

Contents:

.. code-block:: rs

    use thiserror::Error;

#[derive(Debug, Error)]
pub enum ConfigError {
    #[error("Could not parse the config file ({0})")]
    ParseError(String),

    #[error("Missing configuration file '{0}'")]
    MissingFileError(String),

    #[error("The configuration file path is invalid ('{0}' is a directory)")]
    InvalidPathError(String),

    #[error("Could not open config file '{0}'")]
    PermissionError(String),

    #[error("Invalid cluster '{0}'")]
    InvalidCluster(String),

    #[error("Invalid upload method '{0}'")]
    InvalidUploadMethod(String),

    #[error("Invalid token standard '{0}'")]
    InvalidTokenStandard(String),
}


