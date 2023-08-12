library/test/src/helpers/exit_code.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Helper module to detect subprocess exit code.

use std::process::ExitStatus;

#[cfg(not(unix))]
pub fn get_exit_code(status: ExitStatus) -> Result<i32, String> {
    status.code().ok_or_else(|| "received no exit code from child process".into())
}

#[cfg(unix)]
pub fn get_exit_code(status: ExitStatus) -> Result<i32, String> {
    use std::os::unix::process::ExitStatusExt;
    match status.code() {
        Some(code) => Ok(code),
        None => match status.signal() {
            Some(signal) => Err(format!("child process exited with signal {signal}")),
            None => Err("child process exited with unknown signal".into()),
        },
    }
}


