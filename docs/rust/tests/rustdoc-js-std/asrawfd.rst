tests/rustdoc-js-std/asrawfd.js
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    // ignore-order

const QUERY = 'RawFd::as_raw_fd';

const EXPECTED = {
    'others': [
        // Reproduction test for https://github.com/rust-lang/rust/issues/78724
        // Validate that type alias methods get the correct path.
        { 'path': 'std::os::fd::AsRawFd', 'name': 'as_raw_fd' },
        { 'path': 'std::os::fd::AsRawFd', 'name': 'as_raw_fd' },
        { 'path': 'std::os::linux::process::PidFd', 'name': 'as_raw_fd' },
        { 'path': 'std::os::fd::RawFd', 'name': 'as_raw_fd' },
    ],
};


