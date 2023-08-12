src/amman/components/TransactionsMonitorView.tsx
================================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import { Link } from "react-router-dom";
import { useCustomAddressLabels, useTransactionsMonitor } from "../providers";
import { TransactionInfo, TransactionsMonitor } from "../TransactionsMonitor";
import { SnapshotButton } from "./SnapshotButton";

export function TransactionsMonitorView() {
  const [transactionInfos] = useTransactionsMonitor();
  const [customAddressLabels] = useCustomAddressLabels();

  function loadHistory() {
    // TODO(thlorenz): Eventually hould add some kind of indicator that this is
    // loading since this can take quite a while
    TransactionsMonitor.existingInstance.loadTransactionHistory();
  }
  const loadedTxHistory =
    TransactionsMonitor.existingInstance.loadedTransactionHistory;

  const linkLabel = !loadedTxHistory ? (
    <Link
      className="fs-5 d-inline ms-4 text-muted float-end"
      to={"#"}
      onClick={loadHistory}
    >
      Load History
    </Link>
  ) : null;

  return (
    <div className="header-signatures container my-4">
      <h5 className="d-inline">Recent Transactions</h5>
      <SnapshotButton className="fs-5 d-inline ms-4 text-muted float-end" />
      {linkLabel}
      <div className="row align-items-center">
        {transactionInfos.map((x) => TransactionView(x, customAddressLabels))}
      </div>
    </div>
  );
}

function TransactionView(
  x: TransactionInfo,
  customAddressLabels: Map<string, string>
) {
  const statusClass = x.err != null ? "text-warning" : "";
  let label = (
    <p
      className={`display-6 text-truncate ${statusClass}`}
      style={{ maxWidth: 255 }}
    >
      {x.index}. {x.signature}
    </p>
  );
  const addressLabel = customAddressLabels.get(x.signature);
  if (addressLabel != null) {
    label = (
      <div>
        <span className={statusClass}>
          {x.index}. {addressLabel}
        </span>
        <p
          className="opacity-25 display-6 text-truncate"
          style={{ maxWidth: 250 }}
        >
          {x.signature}
        </p>
      </div>
    );
  }
  return (
    <Link className="col-md" key={x.signature} to={"/tx/" + x.signature}>
      {label}
    </Link>
  );
}


