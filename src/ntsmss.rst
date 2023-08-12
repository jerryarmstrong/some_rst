src/ntsmss.rs
=============

Last edited: 2023-04-20 23:00:37

Contents:

.. code-block:: rs

    use crate::ntlpcapi::PPORT_MESSAGE;
use winapi::shared::minwindef::DWORD;
use winapi::shared::ntdef::{HANDLE, NTSTATUS, PHANDLE, PUNICODE_STRING};
EXTERN!{extern "system" {
    fn RtlConnectToSm(
        ApiPortName: PUNICODE_STRING,
        ApiPortHandle: HANDLE,
        ProcessImageType: DWORD,
        SmssConnection: PHANDLE,
    ) -> NTSTATUS;
    fn RtlSendMsgToSm(
        ApiPortHandle: HANDLE,
        MessageData: PPORT_MESSAGE,
    ) -> NTSTATUS;
}}


