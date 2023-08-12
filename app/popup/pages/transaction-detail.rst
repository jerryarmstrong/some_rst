app/popup/pages/transaction-detail.tsx
======================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React, { useEffect, useState } from "react"
import Paper from "@material-ui/core/Paper"
import { ConfirmedTransaction } from "@solana/web3.js"
import { Typography } from "@material-ui/core"
import { withLayout } from "../components/layout"
import { useParams } from "react-router"
import { ArrowBackIos } from "@material-ui/icons"
import { useHistory } from "react-router-dom"
import { Links } from "../components/routes/paths"
import { makeStyles } from "@material-ui/core/styles"
import AppBar from "@material-ui/core/AppBar"
import Toolbar from "@material-ui/core/Toolbar"
import IconButton from "@material-ui/core/IconButton"
import Container from "@material-ui/core/Container"
import Grid from "@material-ui/core/Grid"
import { useConnection } from "../context/connection"
import { createLogger } from "../../core/utils"
import ListItem from "@material-ui/core/ListItem"
import ListItemText from "@material-ui/core/ListItemText"
import List from "@material-ui/core/List"
import { useProgramPluginManager } from "../context/plugins"
import { Markdown } from "../../core/types"
import ReactMarkdown from "react-markdown"
import { formatSolAmount } from "../utils/format"

const log = createLogger("sol:trxDetail")

const useStyles = makeStyles((theme) => ({
  itemDetails: {
    marginLeft: theme.spacing(3),
    marginRight: theme.spacing(3),
    marginBottom: theme.spacing(3),
  },
  accountAddress: {
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(3),
  },

  buttonContainer: {
    display: "flex",
    justifyContent: "space-evenly",
    marginTop: theme.spacing(1),
    marginBottom: theme.spacing(1),
  },
}))

const TransactionDetailBase: React.FC = () => {
  const classes = useStyles()
  let { transactionID, accountAddress, signerAddress } = useParams()
  const { connection } = useConnection()
  const programPluginManager = useProgramPluginManager()
  const [trx, setConfirmedTransaction] = useState<ConfirmedTransaction>()
  const [instructionMarkdowns, setInstructionMardowns] = useState<Markdown[]>([])

  const history = useHistory()

  useEffect(() => {
    log("fetching confirmed transaction:", transactionID)
    connection.getConfirmedTransaction(transactionID).then((ct) => {
      log("confirmed transaction response: %O", ct)
      if (ct) {
        setConfirmedTransaction(ct)
      }
    })
  }, [transactionID, connection])

  useEffect(() => {
    if (!trx || !programPluginManager) {
      return
    }

    log("rendering transaction instruction mark down")
    programPluginManager
      .renderTransactionItemMarkdown(trx.transaction)
      .then((markDowns) => {
        log("get rendered transaction instruction mark down: %O", markDowns)
        setInstructionMardowns(markDowns)
      })
      .catch(log)
  }, [trx, programPluginManager])

  const goBack = () => {
    history.push(
      Links.accountDetail({ accountAddress: accountAddress, signerAddress: signerAddress })
    )
  }

  return (
    <Container fixed maxWidth="md">
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper>
            <AppBar position="static" color="default" elevation={1}>
              <Toolbar>
                <IconButton onClick={goBack}>
                  <ArrowBackIos />
                </IconButton>
                <Typography variant="h6" component="h2" style={{ flexGrow: 1 }}>
                  Transaction Detail
                </Typography>
              </Toolbar>
            </AppBar>
            <div className={classes.itemDetails}>
              <Typography align="center" className={classes.accountAddress} noWrap={true}>
                {transactionID}
              </Typography>
            </div>
            {trx?.transaction && (
              <div className={classes.itemDetails}>
                <Typography>Slot: {trx.slot}</Typography>
                <Typography>Recent Block Hash: {trx.transaction.recentBlockhash}</Typography>
              </div>
            )}

            {trx?.meta && (
              <div className={classes.itemDetails}>
                <Typography>Fee: {formatSolAmount(trx.meta.fee)}</Typography>
                {/*<Typography>*/}
                {/*  Balance Pre/ Post: {amountToSolDecimalString(confirmedTransaction.meta.preBalances)}*/}
                {/*</Typography>*/}
              </div>
            )}
            <Typography variant={"h5"} align={"center"}>
              Instruction
            </Typography>
            <List disablePadding>
              {instructionMarkdowns.length > 0 &&
                instructionMarkdowns.map((instructionMarkdown, index) => (
                  <InstructionListItem key={index} instructionMarkdown={instructionMarkdown} />
                ))}
            </List>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  )
}

interface InstructionListItemProps {
  instructionMarkdown: Markdown
}

const renderInstruction = (content: string) => {
  return (
    <div style={{ overflow: "hidden", wordWrap: "break-word" }}>
      <ReactMarkdown source={content} escapeHtml={false} />
    </div>
  )
}
const InstructionListItem: React.FC<InstructionListItemProps> = ({ instructionMarkdown }) => {
  return (
    <ListItem divider={true}>
      <ListItemText
        primary={renderInstruction(instructionMarkdown)}
        // secondary={
        //   <React.Fragment>
        //     <Typography
        //       className={classes.publicKey}
        //       component="span"
        //       variant="body2"
        //       color="textPrimary"
        //     >
        //       {publicKey.toBase58()}
        //     </Typography>
        //   </React.Fragment>
        // }
        // secondaryTypographyProps={{ className: classes.address }}
      />
    </ListItem>
  )
}

export const TransactionDetail = withLayout(TransactionDetailBase)


