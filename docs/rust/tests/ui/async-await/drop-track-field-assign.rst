tests/ui/async-await/drop-track-field-assign.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Derived from an ICE found in tokio-xmpp during a crater run.
// edition:2021
// compile-flags: -Zdrop-tracking
// build-pass

#![allow(dead_code)]

#[derive(Clone)]
struct InfoResult {
    node: Option<String>
}

struct Agent {
    info_result: InfoResult
}

impl Agent {
    async fn handle(&mut self) {
        let mut info = self.info_result.clone();
        info.node = Some("bar".into());
        let element = parse_info(info);
        let _ = send_element(element).await;
    }
}

struct Element {
}

async fn send_element(_: Element) {}

fn parse(_: &[u8]) -> Result<(), ()> {
    Ok(())
}

fn parse_info(_: InfoResult) -> Element {
    Element { }
}

fn main() {
    let mut agent = Agent {
        info_result: InfoResult { node: None }
    };
    let _ = agent.handle();
}


