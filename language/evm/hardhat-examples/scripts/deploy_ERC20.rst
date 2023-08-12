language/evm/hardhat-examples/scripts/deploy_ERC20.js
=====================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: js

    async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const weiAmount = (await deployer.getBalance()).toString();

  console.log("Account balance:", (await ethers.utils.formatEther(weiAmount)));

  const Token = await ethers.getContractFactory("ERC20Mock"); // A Move contract
  const token = await Token.deploy("MoveOnEvm", "MOE", deployer.address, BigInt(42000 * 10**18));

  console.log("Token address:", token.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
});


