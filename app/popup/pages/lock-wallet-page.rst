app/popup/pages/lock-wallet-page.tsx
====================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React, { useEffect } from "react"
import { Link as RouterLink } from "react-router-dom"
import { Paths } from "../components/routes/paths"
import { withLayout } from "../components/layout"
import { useCallAsync } from "../utils/notifications"
import { useBackground } from "../context/background"
import Card from "@material-ui/core/Card"
import CardContent from "@material-ui/core/CardContent"
import { Typography } from "@material-ui/core"
import CardActions from "@material-ui/core/CardActions"
import Button from "@material-ui/core/Button"

const LockWalletPageBase: React.FC = () => {
  const callAsync = useCallAsync()
  const { request } = useBackground()

  useEffect(() => {
    callAsync(request("popup_lockWallet", {}), {
      progress: { message: "locking wallet..." },
      success: { message: "Wallet locked" },
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <Card>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          Your wallet is locked
        </Typography>
      </CardContent>
      <CardActions style={{ justifyContent: "flex-end" }}>
        <Button color="primary" component={RouterLink} to={Paths.accounts}>
          Unlock
        </Button>
      </CardActions>
    </Card>
  )
}

export const LockWalletPage = withLayout(LockWalletPageBase)


