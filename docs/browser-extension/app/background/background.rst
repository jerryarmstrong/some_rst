app/background/background.ts
============================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import SolanaController from "./solana-controller"
import { createLogger, isInternalProcess } from "../core/utils"
import {
  ENVIRONMENT_TYPE_NOTIFICATION,
  ENVIRONMENT_TYPE_POPUP,
  StoredData,
  VersionedData,
} from "../core/types"
import LocalStore from "./lib/local-store"
import initialState from "./first-time-state"

const PortStream = require("extension-port-stream")
const endOfStream = require("end-of-stream")
const log = createLogger("sol:bg")

const localStore = new LocalStore()
let versionedData: VersionedData

initialize().catch((err) => {
  log("Background initialization failed: %O", err)
})

async function initialize() {
  const versionedData = await loadStateFromPersistence()
  await setupController(versionedData)
}

async function loadStateFromPersistence(): Promise<VersionedData> {
  // migrations
  /*const migrator = new Migrator({ migrations })
  migrator.on('error', console.warn)*/

  // read from disk
  // first from preferred, async API:
  const data = await localStore.get()
  if (!data) {
    versionedData = { version: "1.0", data: initialState }
    log("Solana Empty vault found defaulting to initial state")
  } else {
    log("Solana restoring vault")
    versionedData = data
  }

  // // report migration errors to seError in invocationntry
  // migrator.on('error', (err) => {
  //   // get vault structure without secrets
  //   const vaultStructure = getObjStructure(versionedData)
  //   sentry.captureException(err, {
  //     // "extra" key is required by Sentry
  //     extra: { vaultStructure },
  //   })
  // })

  // migrate data
  // versionedData = await migrator.migrateData(versionedData)
  // if (!versionedData) {
  //   throw new Error('MetaMask - migrator returned undefined')
  // }

  // // write to disk
  // if (localStore.isSupported) {
  //   resp = wait localStore.set(versionedData)
  // } else {
  //   // throw in setTimeout so as to not block boot
  //   setTimeout(() => {
  //     throw new Error("Solana Localstore not supported")
  //   })
  // }

  // return just the data
  return versionedData
}

function setupController(versionedData: VersionedData) {
  log("Setting up controller initial state: %O", versionedData)

  const persistData = async (data: StoredData): Promise<boolean> => {
    if (!data) {
      throw new Error("Solana - updated state does not have data")
    }
    versionedData.data = data

    if (localStore.isSupported) {
      try {
        await localStore.set(versionedData)
        return true
      } catch (err) {
        log("error setting state in local store:", err)
        return false
      }
    }
    return false
  }

  const solanaController = new SolanaController({
    storedData: versionedData.data,
    persistData: persistData,
  })

  function connectRemote(remotePort: chrome.runtime.Port) {
    const processName = remotePort.name
    const tabId = remotePort.sender?.tab?.id
    const url = new URL(remotePort.sender?.url || "")
    const { origin } = url

    if (isInternalProcess(processName)) {
      const portStream = new PortStream(remotePort)
      log(`connect internal process: %o`, {
        processName: processName,
        tabId: tabId,
        url: url,
        origin: origin,
      })
      solanaController.setupTrustedCommunication(processName, portStream, remotePort.sender)
      if (processName === ENVIRONMENT_TYPE_POPUP) {
        solanaController.setPopupOpen()
        endOfStream(portStream, () => {
          solanaController.setPopupClose()
          log("Popup remote stream has ended")
        })
      }

      if (processName === ENVIRONMENT_TYPE_NOTIFICATION) {
        endOfStream(portStream, () => {
          log("Notification remote stream has ended")
        })
      }
    } else if (remotePort.sender && remotePort.sender.tab && remotePort.sender.url) {
      const tabId = remotePort.sender.tab.id
      const url = new URL(remotePort.sender.url)
      const { origin } = url
      log(`connect remote process: %o`, {
        processName: remotePort.name,
        tabId: tabId,
        url: url,
        origin: origin,
      })
      remotePort.onMessage.addListener((msg) => {
        log("received message from remote port [%s]: %O}", remotePort.name, msg)
      })
      connectExternal(remotePort)
    }
  }

  function connectExternal(remotePort: chrome.runtime.Port) {
    const portStream = new PortStream(remotePort)
    solanaController.setupUntrustedCommunication(portStream, remotePort.sender)
  }

  chrome.runtime.onConnect.addListener(connectRemote)
  chrome.runtime.onConnectExternal.addListener(connectExternal)

  return Promise.resolve()
}


