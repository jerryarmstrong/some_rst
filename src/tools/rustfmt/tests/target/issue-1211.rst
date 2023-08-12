src/tools/rustfmt/tests/target/issue-1211.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for iface in &ifaces {
        match iface.addr {
            get_if_addrs::IfAddr::V4(ref addr) => match addr.broadcast {
                Some(ip) => {
                    sock.send_to(&buf, (ip, 8765)).expect("foobar");
                }
                _ => (),
            },
            _ => (),
        };
    }
}


