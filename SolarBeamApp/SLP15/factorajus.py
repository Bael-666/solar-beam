def main():

    pct20 = 20*gcel/(70000*gpot + 40*geea + 20*gcel)
    vpnusd = 6.8578 + pct20*0.6752
    vpnmxn = 6.7917 + pct20*0.6623
    facdevesp = vpnusd/vpnmxn
    nppaq = (ppaq + geea*pml*tcusd)*(1.01*facdevesp)^indexusd

    return facdevesp, pct20, nppaq