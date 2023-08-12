app/popup/components/dialogs/update-token-dialog.tsx
====================================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React, { useState } from "react"
import DialogActions from "@material-ui/core/DialogActions"
import Button from "@material-ui/core/Button"
import DialogTitle from "@material-ui/core/DialogTitle"
import DialogContent from "@material-ui/core/DialogContent"
import TextField from "@material-ui/core/TextField"
import { DialogForm } from "./dialog-form"
import { useCallAsync } from "../../utils/notifications"
import { DialogProps } from "@material-ui/core"
import { useBackground } from "../../context/background"
import { Token } from "../../../core/types"

export type Props = Omit<DialogProps, "onClose"> & {
  token: Token
  onClose: () => void
}

export const UpdateTokenDialog: React.FC<Props> = ({ token, open, onClose, children, ...rest }) => {
  const callAsync = useCallAsync()
  const { request } = useBackground()
  const oldMint = token.mintAddress
  let [mintAddress, setMintAddress] = useState(oldMint)
  let [tokenName, setTokenName] = useState(token.name)
  let [tokenSymbol, setTokenSymbol] = useState(token.symbol)
  let [sending, setSending] = useState(false)

  const canSend = (): boolean => {
    return mintAddress !== "" && tokenName !== "" && tokenSymbol !== ""
  }

  const onSubmit = () => {
    setSending(true)
    callAsync(
      request("popup_updateToken", {
        mintAddress: oldMint,
        token: {
          mintAddress: mintAddress,
          name: tokenName,
          symbol: tokenSymbol,
        },
      }),
      {
        progress: { message: "Updating token..." },
        success: { message: "Success!" },
        onFinish: () => {
          setSending(false)
          onClose()
        },
      }
    )
  }

  return (
    <DialogForm open={open} onClose={onClose} onSubmit={onSubmit} {...rest}>
      <DialogTitle>Add Token</DialogTitle>
      <DialogContent>
        <TextField
          label="Token Mint Address"
          fullWidth
          variant="outlined"
          margin="normal"
          value={mintAddress}
          onChange={(e) => setMintAddress(e.target.value)}
        />
        <TextField
          label="Token Name"
          fullWidth
          variant="outlined"
          margin="normal"
          value={tokenName}
          onChange={(e) => setTokenName(e.target.value)}
        />
        <TextField
          label="Token Symbol"
          fullWidth
          variant="outlined"
          margin="normal"
          value={tokenSymbol}
          onChange={(e) => setTokenSymbol(e.target.value)}
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button type="submit" color="primary" disabled={!canSend || sending}>
          Add
        </Button>
      </DialogActions>
    </DialogForm>
  )
}


