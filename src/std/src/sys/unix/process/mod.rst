src/std/src/sys/unix/process/mod.rs
===================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    pub use self::process_common::{Command, CommandArgs, ExitCode, Stdio, StdioPipes};
pub use self::process_inner::{ExitStatus, Process};
pub use crate::ffi::OsString as EnvKey;
pub use crate::sys_common::process::CommandEnvs;

mod process_common;
#[cfg(not(target_os = "fuchsia"))]
#[path = "process_unix.rs"]
mod process_inner;
#[cfg(target_os = "fuchsia")]
#[path = "process_fuchsia.rs"]
mod process_inner;
#[cfg(target_os = "fuchsia")]
mod zircon;


