app/popup/components/dialogs/dialog-form.tsx
============================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React from "react"
import Dialog, { DialogProps } from "@material-ui/core/Dialog"

export const DialogForm: React.FC<DialogProps> = ({
  open,
  onClose,
  onSubmit,
  children,
  ...rest
}) => (
  <Dialog
    open={open}
    PaperProps={{
      component: "form",
      onSubmit: (e) => {
        e.preventDefault()
        if (onSubmit) {
          onSubmit(e)
        }
      },
    }}
    onClose={onClose}
    {...rest}
  >
    {children}
  </Dialog>
)


