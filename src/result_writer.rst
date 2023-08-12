src/result_writer.rs
====================

Last edited: 2023-05-15 14:19:21

Contents:

.. code-block:: rs

    use crate::states::{BlockData, TransactionConfirmRecord};
use async_std::fs::File;
use tokio::{sync::broadcast::Receiver, task::JoinHandle};

pub fn initialize_result_writers(
    transaction_save_file: String,
    block_data_save_file: String,
    tx_data: Receiver<TransactionConfirmRecord>,
    block_data: Receiver<BlockData>,
) -> Vec<JoinHandle<()>> {
    let mut tasks = vec![];

    if !transaction_save_file.is_empty() {
        let tx_data_jh = tokio::spawn(async move {
            let mut writer = csv_async::AsyncSerializer::from_writer(
                File::create(transaction_save_file).await.unwrap(),
            );
            let mut tx_data = tx_data;
            loop {
                if let Ok(record) = tx_data.recv().await {
                    writer.serialize(record).await.unwrap();
                } else {
                    break;
                }
            }
            writer.flush().await.unwrap();
        });
        tasks.push(tx_data_jh);
    }

    if !block_data_save_file.is_empty() {
        let block_data_jh = tokio::spawn(async move {
            let mut writer = csv_async::AsyncSerializer::from_writer(
                File::create(block_data_save_file).await.unwrap(),
            );
            let mut block_data = block_data;
            loop {
                if let Ok(record) = block_data.recv().await {
                    writer.serialize(record).await.unwrap();
                } else {
                    break;
                }
            }
            writer.flush().await.unwrap();
        });
        tasks.push(block_data_jh);
    }
    tasks
}


