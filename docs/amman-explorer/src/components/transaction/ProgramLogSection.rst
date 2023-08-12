src/components/transaction/ProgramLogSection.tsx
================================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { SignatureProps } from "pages/TransactionDetailsPage";
import { useTransactionDetails } from "providers/transactions";
import { ProgramLogsCardBody } from "components/ProgramLogsCardBody";
import { prettyProgramLogs } from "utils/program-logs";
import { useCluster } from "providers/cluster";

export function ProgramLogSection({ signature }: SignatureProps) {
  const { cluster } = useCluster();
  const details = useTransactionDetails(signature);

  const transaction = details?.data?.transaction;
  if (!transaction) return null;
  const message = transaction.transaction.message;

  const logMessages = transaction.meta?.logMessages || null;
  const err = transaction.meta?.err || null;

  let prettyLogs = null;
  if (logMessages !== null) {
    prettyLogs = prettyProgramLogs(logMessages, err, cluster);
  }

  return (
    <>
      <div className="card">
        <div className="card-header">
          <h3 className="card-header-title">Program Logs</h3>
        </div>
        {prettyLogs !== null ? (
          <ProgramLogsCardBody
            message={message}
            logs={prettyLogs}
            cluster={cluster}
          />
        ) : (
          <div className="card-body">
            Logs not supported for this transaction
          </div>
        )}
      </div>
    </>
  );
}


