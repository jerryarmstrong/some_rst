src/amman/components/SnapshotButton.tsx
=======================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import { ChangeEvent, useState } from "react";
import { AmmanClient } from "../amman-client";

const DISK_SAVE_EMOJI = "💾";

export function SnapshotButton(props: { className: string }) {
  const [showDialog, setShowDialog] = useState(false);
  const [label, setLabel] = useState("");
  const [savedAs, setSavedAs] = useState<string | null>(null);

  function onLabelChanged(event: ChangeEvent<HTMLInputElement>) {
    setLabel(event.target.value);
  }

  async function onSave() {
    const withoutWhiteSpace = label.replace(/\s/g, "-");
    await AmmanClient.instance.saveSnapshot(withoutWhiteSpace);
    setSavedAs(withoutWhiteSpace);
  }

  let dialog;
  if (showDialog) {
    let dialogContent =
      savedAs == null ? (
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title" id="exampleDialogLabel">
              Save Snapshot
            </h5>
          </div>
          <div className="modal-body">
            <input
              type="text"
              className="form-control"
              autoFocus
              onChange={onLabelChanged}
            />
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => setShowDialog(false)}
            >
              Cancel
            </button>
            <button type="button" className="btn btn-primary" onClick={onSave}>
              Save
            </button>
          </div>
        </div>
      ) : (
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Successfully Saved Snapshot</h5>
          </div>
          <div className="modal-body">
            <div>Load it when starting amman via:</div>
            <pre className='mt-4 p-3'>amman start --load {savedAs}</pre>
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => {
                setShowDialog(false);
                setSavedAs(null);
              }}
            >
              Close
            </button>
          </div>
        </div>
      );
    dialog = <div className="modal-dialog modal-centered">{dialogContent}</div>;
  }
  return (
    <>
      {dialog}
      <div
        className={props.className}
        role="button"
        onClick={() => setShowDialog(true)}
      >
        {DISK_SAVE_EMOJI}
      </div>
    </>
  );
}


