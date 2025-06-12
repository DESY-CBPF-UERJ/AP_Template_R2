analysis = "AP_Template_R2"
nano_version = 'v9'

#--------------------------------------------------------------------------------------------------
# Production ID:
# 00-09(Data), 10-19(MC-signal), 20-98(MC-bkg), 99(private sample)
#
# Data taking interval (DTI):
# 2016 DTIs = 0(with "HIPM"/"APV")("pre-VFP"), 1(without "HIPM"/"APV")("pos-VFP")
#--------------------------------------------------------------------------------------------------

paths = {}
paths["0_16"] = analysis+'/Datasets/Files/bkg_16/dti_0/'+nano_version+'/'
paths["1_16"] = analysis+'/Datasets/Files/bkg_16/dti_1/'+nano_version+'/'
paths["0_17"] = analysis+'/Datasets/Files/bkg_17/dti_0/'+nano_version+'/'
paths["0_18"] = analysis+'/Datasets/Files/bkg_18/dti_0/'+nano_version+'/'


# https://xsecdb-xsdb-official.app.cern.ch/
# Source[*] > > https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
# Source[**] > > https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG
# Source[new1] > > https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
# Source[new2] > > https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO
# Source[new3] > > https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
b_ds_info = { # [DatasetName, Production ID, PROC_XSEC[pb], XSEC_UNC[pb], XSEC_Accuracy]
"TTFullLep": [
    ["TTTo2L2Nu",                           '22',       88.51,              0,                  '[new2]NNLO+NNLL'],
],

"VZ": [
    ["ZZTo2L2Nu",                           '25',       0.9738,             0.0009971,          'NLO'],
    ["ZZTo4L",                              '25',       1.325,              0.00122,            'NLO'],
    ["WZTo3LNu",                            '25',       4.664,              0.004639,           'NLO'],
],
}


#----------------------------------------------------------------------------------------
# [DO NOT TOUCH THIS PART]
#----------------------------------------------------------------------------------------
b_ds = {}
for period in paths.keys():

    dti = period[0]
    year = period[-2:]

    for key in b_ds_info.keys():
        b_ds[key+"_"+period] = []
        for ds in b_ds_info[key]:
            list_temp = []
            list_temp.append(ds[0]+"_"+period)
            list_temp.append(ds[1]+year+dti)
            list_temp.append(paths[period]+ds[0]+".txt")
            list_temp.append(ds[2])
            list_temp.append(ds[3])
            b_ds[key+"_"+period].append(list_temp)

