# Given: A protein string of length at most 1000 aa.
# 
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
# (Don't neglect the importance of the stop codon in protein translation.)

aaDic = {
'F' : 2, 'L' : 6, 'I' : 3, 'M' : 1, 'V' : 4, 'S' : 6, 'P' : 4, 'T' : 4, 'A' : 4, 'Y' : 2, 'H' : 2, 'Q' : 2, 'N' : 2, 'K' : 2, 'D' : 2, 'E' : 2, 'C' : 2, 'W' : 1, 'R' : 6, 'G' : 4
}

aa = "MWNQTMTVSKMEPEAIKCHMHVPDYHTYEVTTTRHNFIETMKPSYMGWPSTHSNWTEAPACRQIKQRRKGDCVMVPVCHSWTKQWSAMDPKCVDNLEGCLFFLAKMHLVCINHFYCTFHTRQGIIFFPGYRGAGMAEAHRKVTVIKHYFFNSIQHNQPKVDEWSRCLAVVSFLGIEMTHLVYKANCLVWCFNHFWYIDWFQLGWRICVQRTAETMMVGPHRCAVPTSDCWVVVKFKCPLFKNIPANTQYIPIDGEGLWQHQRHYEGWGRICACNKWFNADPCNLRMCMQCIHIVVQNYQKCYPDIYIKCQKLWFYFVVSCPDEIDCSCPYCNHIFGCFVANRWYPMIPYQIPWFIDWNWTLGIFQGVPSVRESIGGTGANVPFVGCYVYRMAYCPFDWTTMCADGVVCCLLKDFMRPLSGTEMWIYMMSDFFMRTFKSLMERFTENDKWLAQIVFYQIIQTSINMTLGAKVSEYCNQEWNKYDKQYSKVSGREEGVNLCDWSQFKRLCLCLYGNAQRKVRHISTSENHWMFGYNEDYSVPYNNLNTCDSQAPCMAQKVICNFQCGAIECTKDTVADILWWRSSCHHNHGPPDRDPCSLNYPPNAAVAVRNCWGDCWQKWDGMRWLVTRACINNQLPSPFYWKRKPQATTHICIHSFAIRTGWQLLLSEGALIMLLNGSWVEFLCGQRDMTEHPRCAGYTQFCTCFCNQNQHMMWKTLHQMREDDRSKCDDPWGHNCDSGHAVQASVKECFRCILSHYVEEAEWGEATIVCVHRERSSTFWGGQRLQLVTFMLRSYTGGWKYSRPTVITYAIPIDGDEPHHIIQCHPMVIGWPNGEFKGAFMEKVWWEKPVQGDHAWEAEIHPRMSIQTAVPQRRDGWAHMPTIDPNNERPPFWYTEEWTGDHNPIFGIDFVWLWDPKYNAHDYTYIEHMHGKFRCMYRHPRINQTNTQGCCDCDREMGMDLEPPKNYSSWRTQLLFPGYKAMEGYPCCMERVWAEWCHEA"
rst = 1
for i in aa :
    rst *= aaDic[i]

rst *= 3
rrst = rst % 1000000   
print(rrst)
