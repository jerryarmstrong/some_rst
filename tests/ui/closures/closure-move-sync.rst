tests/ui/closures/closure-move-sync.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::thread;
use std::sync::mpsc::channel;

fn bar() {
    let (send, recv) = channel();
    let t = thread::spawn(|| {
        recv.recv().unwrap();
        //~^^ ERROR `std::sync::mpsc::Receiver<()>` cannot be shared between threads safely
    });

    send.send(());

    t.join().unwrap();
}

fn foo() {
    let (tx, _rx) = channel();
    thread::spawn(|| tx.send(()).unwrap());
    //~^ ERROR `Sender<()>` cannot be shared between threads safely
}

fn main() {}


