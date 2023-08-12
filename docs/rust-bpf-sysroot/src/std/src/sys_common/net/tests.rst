src/std/src/sys_common/net/tests.rs
===================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use super::*;
use crate::collections::HashMap;

#[test]
fn no_lookup_host_duplicates() {
    let mut addrs = HashMap::new();
    let lh = match LookupHost::try_from(("localhost", 0)) {
        Ok(lh) => lh,
        Err(e) => panic!("couldn't resolve `localhost': {}", e),
    };
    for sa in lh {
        *addrs.entry(sa).or_insert(0) += 1;
    }
    assert_eq!(
        addrs.iter().filter(|&(_, &v)| v > 1).collect::<Vec<_>>(),
        vec![],
        "There should be no duplicate localhost entries"
    );
}


