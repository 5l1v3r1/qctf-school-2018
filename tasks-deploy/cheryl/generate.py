TITLE = "День рождения Черил"
STATEMENT_TEMPLATE = '''
Описание таска.

[Сайт](https://cheryl.contest.qctf.ru)
Login: {}
Password: {}
'''

def generate(context):
    participant = context['participant']
    data = team_data[participant.id % len(team_data)][:2]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(*data))

team_data = [('i5rSrsFHqz7fBQO7KqXx', 'Xl0R2VZzhe', 'QCTF{Alb3r7_Rwk6qsgMIH_B3rn4rd}'), ('MxXyFnkuTplJBNHLso8N', 'GWxCrYtrLi', 'QCTF{Alb3r7_LxOFZJmKjF_B3rn4rd}'), ('q3eUYw7zEaD5kprz1WxI', 'EbWuNBKiyl', 'QCTF{Alb3r7_EToWE2FDu4_B3rn4rd}'), ('vlrN0773CskNPiVLQES8', 'icFrgeQmDi', 'QCTF{Alb3r7_4T3I1p3x8a_B3rn4rd}'), ('TN1QKCfEwk4Xs1Ey4TKW', 'uNte6ah3ty', 'QCTF{Alb3r7_q7RrPfHP0r_B3rn4rd}'), ('Tc0q7Z557MjHFd07PIed', 'QjRJySHek3', 'QCTF{Alb3r7_qtbCNVfL1G_B3rn4rd}'), ('kgW9X6jTBhobeCPmlhl2', 'EkMMiQ4dn5', 'QCTF{Alb3r7_SHwf8pDgEP_B3rn4rd}'), ('vXlXvys4hCyfDoru2JJ8', '3tFA1Wipmc', 'QCTF{Alb3r7_IcXOJQ32C6_B3rn4rd}'), ('Vp7BtSKwa8HOWFtTU6ad', 'OhfmumubTL', 'QCTF{Alb3r7_IrQez4Oh0g_B3rn4rd}'), ('D4XQQ8HOSzxwusqidUOh', 'J2dyLyRg1T', 'QCTF{Alb3r7_l7QSa0W3it_B3rn4rd}'), ('qDWytCeZaNX5RDZOS8Zx', 'eg9rFTNp7s', 'QCTF{Alb3r7_ISlROcoGjl_B3rn4rd}'), ('DjSYDBlPUHgV9LkJNyMb', '93i8bnzZvT', 'QCTF{Alb3r7_eG5DdNJhEe_B3rn4rd}'), ('qU3XAC05yPaEiXNhgHw0', 'vRPCfgSKYH', 'QCTF{Alb3r7_sGvmHbi9gt_B3rn4rd}'), ('NEw6Jl6eKQJ3fnpGVLVu', 'rJKNduxikk', 'QCTF{Alb3r7_0MZBfYcVPm_B3rn4rd}'), ('cI0j1VQvlezVnCr5MzfU', 'dcDugpQ4w2', 'QCTF{Alb3r7_azGqKNKiKO_B3rn4rd}'), ('33l1wXc6Zp7oycsCSP9e', 'DP34UVGKED', 'QCTF{Alb3r7_K0uhg9UIMU_B3rn4rd}'), ('kb7iDsROLjjfLyFz1gTw', 'xEXuvzhO4u', 'QCTF{Alb3r7_tWjK4FVHXa_B3rn4rd}'), ('bWE7yRNq2GLEQigw9bWx', 'fLqhwUzD4P', 'QCTF{Alb3r7_3zR06F2Eu7_B3rn4rd}'), ('JNTbyLe5uik3QsYlQejr', 'w21uUQjBu7', 'QCTF{Alb3r7_P7bSCoh9p5_B3rn4rd}'), ('HoF3Z1E9G83yZN09ofD9', 'qnyDBtlZmt', 'QCTF{Alb3r7_ztcMxp1nUE_B3rn4rd}'), ('opA6c7ls5lzhjk5NzzmR', '3cIUAcymbZ', 'QCTF{Alb3r7_q5OSWHGZbt_B3rn4rd}'), ('P0zoBBzuaoyimvQVuC45', 'GLeGVGqnkF', 'QCTF{Alb3r7_5qu8XWx5zc_B3rn4rd}'), ('Vmz51QTAmnZJR71fItoH', 'vOTzIwPikW', 'QCTF{Alb3r7_PGhtRPl4KD_B3rn4rd}'), ('zZhnJQq45Ps1e2Nalm2H', '0NOAkaQmWv', 'QCTF{Alb3r7_aKewR3Ncry_B3rn4rd}'), ('EzSIWX5D0UQ2bt9ALZgh', '0KhEUhFhES', 'QCTF{Alb3r7_fPdUtufWoI_B3rn4rd}'), ('ehB6Uc33oTNVJVz5xUpB', 'whXFia5pCd', 'QCTF{Alb3r7_zAEgEHznce_B3rn4rd}'), ('Mdr128B45wg6nr4jmvFW', 'gBdSZ4jsk5', 'QCTF{Alb3r7_TLgkKdZ5uz_B3rn4rd}'), ('tEiDnV1olHab0TQnRTd8', 'Eswe4Uoixe', 'QCTF{Alb3r7_ufnqy36ohl_B3rn4rd}'), ('yceN7nuKq2EajBBxWNHP', 'b52McMjGSZ', 'QCTF{Alb3r7_Or2fGW9ckd_B3rn4rd}'), ('Pjv0p1dzQamnuq6xprSf', 'rL3q8MH1S5', 'QCTF{Alb3r7_JIkLc7yXl2_B3rn4rd}'), ('jdyTI3XT90yw2d88vG7D', 'LehFi2TaAo', 'QCTF{Alb3r7_pmpE1zxsVb_B3rn4rd}'), ('SLbPaszhSA4vXv9RmhLU', '8ufETzPFgQ', 'QCTF{Alb3r7_92Pn5RIJOw_B3rn4rd}'), ('Oyw2yzGXNGuI70BW7GLi', '2iFOXUauJy', 'QCTF{Alb3r7_EAI10SSE8I_B3rn4rd}'), ('FaZaFIYDlOwfyZuGxtvM', 'zF5FeC3eud', 'QCTF{Alb3r7_8iSyQxW08d_B3rn4rd}'), ('xYuWskxNZnc2cd6qM6W5', 'jjZFkTwpbi', 'QCTF{Alb3r7_zolAZMpCkJ_B3rn4rd}'), ('96DkQeInTgWxdnbyC9Ey', 'ssvWmt2PwK', 'QCTF{Alb3r7_wzwWqodGGY_B3rn4rd}'), ('ToFyQIOjzsPSflV4mwxI', 'cWaEKVJQLy', 'QCTF{Alb3r7_9Dnhsrabd6_B3rn4rd}'), ('3vF3w3IZjabmSP8Tl6cl', 'Qzpnm9hg82', 'QCTF{Alb3r7_RQiGYVZYTB_B3rn4rd}'), ('NmqvNQP7XF871m6feWzA', 'BEC5UIyBQS', 'QCTF{Alb3r7_Au8pucnikF_B3rn4rd}'), ('7WNKSUE89tf0frQxqfPV', 'WOEW9jH2qS', 'QCTF{Alb3r7_ftWZsRTtU0_B3rn4rd}'), ('yCgRfF6ZT54G1hVVCDE7', 'guiFE6Canc', 'QCTF{Alb3r7_OOGUGNWvQv_B3rn4rd}'), ('chrKVUPBIHo5wmwiNeRt', '4KS9Y1oLl2', 'QCTF{Alb3r7_bsVavP3Keu_B3rn4rd}'), ('VxzGueKIQBs5xLgUPwPp', 'czmljvNTrT', 'QCTF{Alb3r7_4PKnW2np0H_B3rn4rd}'), ('8Sr5vDK3dqfX7oATCsS1', '0VRzzoIUC1', 'QCTF{Alb3r7_fFhCgY7CFl_B3rn4rd}'), ('t4Ki9Ol7h9QbuD4pmiYz', 'SwBnZss9AO', 'QCTF{Alb3r7_DbyRjWzlyP_B3rn4rd}'), ('Nhe1wts7lqTC5rnEO92z', 'h07pGpYAM1', 'QCTF{Alb3r7_UfXFCUCCp0_B3rn4rd}'), ('dH2oeuEaKCNk8Vg5q0oQ', 's2vsti92uO', 'QCTF{Alb3r7_ZulPI37PmV_B3rn4rd}'), ('K1NHXILtxCZVgd4sSqZ4', 'IxXEfFuRfD', 'QCTF{Alb3r7_9vcO5Xbo7e_B3rn4rd}'), ('BkHr9DjTqAQ30QMnoucH', 'ISBcLYOObL', 'QCTF{Alb3r7_sTjk8lBTZR_B3rn4rd}'), ('SE6SflSbebwiaZBZMCA6', 'h3475VI5FY', 'QCTF{Alb3r7_VgiUGyxFXu_B3rn4rd}'), ('5wPLHfbtnepb58lE5djv', 'L5i0aFKn3U', 'QCTF{Alb3r7_kYUjAA0UKf_B3rn4rd}'), ('FUBFDuITRbYm6vJXr0Xm', 'eppUygCrdD', 'QCTF{Alb3r7_JY0plJPHCz_B3rn4rd}'), ('Y0u8nyLkbB95qgDMOKZl', 'n58PP7hdxL', 'QCTF{Alb3r7_lM0hrTL8T5_B3rn4rd}'), ('eagKNJFoSQ1XrmobSSfN', 'XTx1jsT39l', 'QCTF{Alb3r7_txJ1w6GcsQ_B3rn4rd}'), ('Pk4D3PbtKFmZPeN83dBi', 'ABwQ5i0XY5', 'QCTF{Alb3r7_EDNK4RL6sL_B3rn4rd}'), ('bNFhFPReOscTUGj3xFBA', 'R4E0P90x9q', 'QCTF{Alb3r7_OsQ661KWiV_B3rn4rd}'), ('nc4vIrpFycqhnhzYz8zD', 'FWMx97dLdl', 'QCTF{Alb3r7_tY9khbBrOk_B3rn4rd}'), ('ktpnN5jiQ4GQv5ldpCkW', 'iW3TfaUM0y', 'QCTF{Alb3r7_xyOV979PYa_B3rn4rd}'), ('PjsmtGRWkeeCqaGnqlPu', 'dsgk9uJnFe', 'QCTF{Alb3r7_2yAJ1HjE8e_B3rn4rd}'), ('Z9ISO94jP7HExu89dVKe', 'KIKr1G4NVP', 'QCTF{Alb3r7_ki8SZAHQrO_B3rn4rd}'), ('F05zVHB2D7L5mvQsMKRs', 'uhCeI5J6wq', 'QCTF{Alb3r7_AA6HOvtmPN_B3rn4rd}'), ('jaDdBcxUQDaB4Ysb57EH', 'kwCCUinoba', 'QCTF{Alb3r7_125Ss2V7rG_B3rn4rd}'), ('nkFG8DnvYdOOF21G4ejR', '20mkRwjfjS', 'QCTF{Alb3r7_hInRJFzoqP_B3rn4rd}'), ('7YEaXyDO2r1fh6ai9TlX', 'adnCNUyKaS', 'QCTF{Alb3r7_CgyavIInGr_B3rn4rd}'), ('0Mf6QO6Gzzd7KdzcrCjM', 'xaKJzRbXte', 'QCTF{Alb3r7_FhZhPAf6aF_B3rn4rd}'), ('arHSqGuIChEqRMlkDbgd', '3Dk2pWf2c1', 'QCTF{Alb3r7_7L00I1moPG_B3rn4rd}'), ('FoxMP9DLvG4mwYYiRxvQ', '3YinkZNFBg', 'QCTF{Alb3r7_KY8HSu7Dyb_B3rn4rd}'), ('xcMHnD2asm3eTt7zQaiB', 'WjZG5wmCnU', 'QCTF{Alb3r7_QfKeuBH0Af_B3rn4rd}'), ('WxnA7w28Y8LOlXllzzqx', 'hLFkREw2wQ', 'QCTF{Alb3r7_SPre3wP5Dq_B3rn4rd}'), ('KwmnySmng88tfpcjmEPZ', 'D2FVeIOXIM', 'QCTF{Alb3r7_3HrPrHTMdB_B3rn4rd}'), ('ucqOmbb4CqYQ14IpABTL', '6ObElpUO9b', 'QCTF{Alb3r7_5JX0KjIYV2_B3rn4rd}'), ('ZTKmLSS03w87qLatmvPX', 'WNVu98zsoi', 'QCTF{Alb3r7_d4RFqIydRj_B3rn4rd}'), ('btgj3X92klbcj52UtPuu', '800Ga0gJhK', 'QCTF{Alb3r7_t4MVJ4fqIS_B3rn4rd}'), ('mc08yIpGc5yfFDNKtmxV', '1GkIax4QB0', 'QCTF{Alb3r7_cp24avV5X4_B3rn4rd}'), ('XyBGrqJrw7U7NNUfBQgl', 'T5X2ei1bL9', 'QCTF{Alb3r7_GjUzjAZpww_B3rn4rd}'), ('zfFZUXZTnkEop7NG0woB', '4DtNHFSbTv', 'QCTF{Alb3r7_6NmbzwsQRB_B3rn4rd}'), ('iGrfhGMSGKDYcwSdtPNG', 'A2VrkzShid', 'QCTF{Alb3r7_OV3ofHvZqH_B3rn4rd}'), ('Tu93amI1BkNMHKx4aBkM', '6zd7gzJO0H', 'QCTF{Alb3r7_Ht2GzCr2nj_B3rn4rd}'), ('XgOpCkinMKRUhPHx0Mf0', 'A3jlqbXrCs', 'QCTF{Alb3r7_0P5BZ9u2lg_B3rn4rd}'), ('PxtG2qdl4U0Z0gKQ63ob', '93KKlnVlUi', 'QCTF{Alb3r7_reB7zg7Ugr_B3rn4rd}'), ('TkWPDtrwQGKua6pWkyeZ', 'ZGAIqIhF2m', 'QCTF{Alb3r7_qpOPLyUl6V_B3rn4rd}'), ('lbQIGogpMoHhZPTqORkt', 'rwBF8tEZbG', 'QCTF{Alb3r7_cOSsHy7n3d_B3rn4rd}'), ('l1akZ9YA78NpyvmhGRg3', 'ugIsDNyYrn', 'QCTF{Alb3r7_Av0k5Slq4n_B3rn4rd}'), ('fL1fd8RQbf0AGCsUYHrn', 'peXBGDj3Xa', 'QCTF{Alb3r7_ybpi0V5Ft5_B3rn4rd}'), ('G0M1qvotX7v4UADOak3P', 'XQ7KwRdD40', 'QCTF{Alb3r7_tUp7VrQ2ku_B3rn4rd}'), ('ibwt1lRxVuPRWRpMVYXW', 'lSYWvnRgt4', 'QCTF{Alb3r7_8pBdmRy8e5_B3rn4rd}'), ('e3RXe2T3RxDTIXb38v2N', '4ccuVj3zFY', 'QCTF{Alb3r7_hGxHoxRBAx_B3rn4rd}'), ('zzznaR4mfTrNBRH8LOoE', 'JCRU2OYI00', 'QCTF{Alb3r7_sNQYBOlLF2_B3rn4rd}'), ('x4Ui5Ac92ofq3a4nZcnj', 'SoZut6dhtU', 'QCTF{Alb3r7_4MRXuiB5q9_B3rn4rd}'), ('TImkZzX3zfsMMghcoS5r', 'JjRgrvmzly', 'QCTF{Alb3r7_WKNgZ8FiqM_B3rn4rd}'), ('wwmLZlYnXlDunRRvYYJL', 'T6r0iyMDF8', 'QCTF{Alb3r7_Oq8is8HaaD_B3rn4rd}'), ('4r5Q1UMzQlgZU5lO4oYJ', 'ewkSJwHlOL', 'QCTF{Alb3r7_D2NaJ4ORBM_B3rn4rd}'), ('lqzlAzu5Ffk9rZtWE988', 'toP5IGB1Vi', 'QCTF{Alb3r7_dW2B0TwUGm_B3rn4rd}'), ('OSwMOEqIFXiDBgcnMKS1', 'FjGUKJEqq9', 'QCTF{Alb3r7_C5k3zq7N59_B3rn4rd}'), ('bayz1tjLHNSG7iEiL76Z', 'rx3rNssykY', 'QCTF{Alb3r7_1CZnsSVFf3_B3rn4rd}'), ('VknvLPqJVbCOtgsgRuNN', 'dDhsd9k31H', 'QCTF{Alb3r7_KcYzPDwIRM_B3rn4rd}'), ('rqlndSHBeKYDjcQiHX3l', 'oG71vwVLlw', 'QCTF{Alb3r7_MoAJzDOs8q_B3rn4rd}'), ('J42qRkWzC0sR3GpspYv6', 'dLd4jmAUKT', 'QCTF{Alb3r7_yK8GdokI8R_B3rn4rd}'), ('Gmzvtq6IdHfB9a08BZoY', 'UST1q6RJAG', 'QCTF{Alb3r7_RhMfOKm0JT_B3rn4rd}'), ('uG7ZQKGYwR6J30mRPoP5', 'swj62NqwKM', 'QCTF{Alb3r7_Exj2F36Bly_B3rn4rd}'), ('9nGxPiKvr0OHZNzQJbBM', 'vpbePf3T1H', 'QCTF{Alb3r7_c1xFwSYZ14_B3rn4rd}'), ('tb2BJf2ZCz0Vw8tO4Sl0', 'WOGzdutoaM', 'QCTF{Alb3r7_6rLUhLQh8J_B3rn4rd}'), ('Fyav8L7G68nsGzQiBobb', '4owIGLAxh9', 'QCTF{Alb3r7_FNMu6nmD9F_B3rn4rd}'), ('2t3ZrsoWh06KMdgy0BNe', 'vmF8HQ9oey', 'QCTF{Alb3r7_tWetJ3dLtp_B3rn4rd}'), ('SYxDrCAvevU5Gl4eI1Bn', 'ES6tfnqP7x', 'QCTF{Alb3r7_V9EKB345Th_B3rn4rd}'), ('6DsyOJNGzuInw5sPfIk4', 'cxr2X7tSpl', 'QCTF{Alb3r7_t1Du0BBvEF_B3rn4rd}'), ('JRybnOYr45Y0jKU7cDoI', 'eljil8yGJI', 'QCTF{Alb3r7_RiVHxwgAJ3_B3rn4rd}'), ('u2IZ54y9LRzreBRr6y31', 'QjgQtoGkaW', 'QCTF{Alb3r7_itREr9iLyh_B3rn4rd}'), ('77kQCXa6sItGt4PG4kX4', 'ONqGRlGCva', 'QCTF{Alb3r7_kO4m90eoBU_B3rn4rd}'), ('VG50CLH9GFkJcxa5fSr8', 's9ZrGItRGP', 'QCTF{Alb3r7_3u5K4grwgd_B3rn4rd}'), ('iATSbWeJkbafor5M3zZj', 'pKohfZQjdf', 'QCTF{Alb3r7_1XRvPWtWXQ_B3rn4rd}'), ('vlAsc7zjn9zTwuVebk5s', 'Hh9hlybFjT', 'QCTF{Alb3r7_fNzHZyehks_B3rn4rd}'), ('XC967cEgVXlBPDvEnxVS', '2rX0Tp87ZG', 'QCTF{Alb3r7_HY6WAOJNoH_B3rn4rd}'), ('j9W1OuOgklzV1Ssyykjz', 'VRGj7UjGo2', 'QCTF{Alb3r7_HLv9R0G8va_B3rn4rd}'), ('NDyz0MsFBgvuReJO2GRV', 'R0mMNEooE1', 'QCTF{Alb3r7_N0H9rcgrjk_B3rn4rd}'), ('e1qmdnUATQfcv8Vt0mJL', 'zDMc6cHpoq', 'QCTF{Alb3r7_HYr3PncMD0_B3rn4rd}'), ('KuWNUnoP9RxCihob7Iat', 'OMGUhbCO2C', 'QCTF{Alb3r7_5QvbrrerLR_B3rn4rd}'), ('DEnlHVRogbbezTSwE8qp', '8omzgxP3Fj', 'QCTF{Alb3r7_sc9RxxNua8_B3rn4rd}'), ('p4ZtWpxJpLtDpKVmP9pa', '6y38PIqNQz', 'QCTF{Alb3r7_UbJ3rD8ZgW_B3rn4rd}'), ('iJSsYwP1A56glxsjApnx', 'pn43sDCzXH', 'QCTF{Alb3r7_6dQdNXMMJ2_B3rn4rd}'), ('wxkaigM6QL9hwmkou2t7', 'eH2xPQmfiY', 'QCTF{Alb3r7_XjocRA6MA0_B3rn4rd}'), ('tDPWQfU6KX3rhfNDzbAX', 'aLycYCYtVn', 'QCTF{Alb3r7_bLf6wTUPaS_B3rn4rd}'), ('hnvs4xlPXr5E3U9jXmVq', 'K38VsjlY08', 'QCTF{Alb3r7_qZ0oA5HEhs_B3rn4rd}'), ('1are6SzLEDsfhsYUao7A', 'S3MEIB6YWa', 'QCTF{Alb3r7_dozJMpcSsQ_B3rn4rd}'), ('5Ly9UA3MZVsE7xcIlTOu', 'nZIR4zqnmg', 'QCTF{Alb3r7_qNzuJ9eSXR_B3rn4rd}'), ('FQJNFGUdkph3U3Oof4P1', 'Ag8DjUcWjm', 'QCTF{Alb3r7_8MsjeEVIc3_B3rn4rd}'), ('JqH9h5msbjatmwuZYPoa', 'SWHFCrepfZ', 'QCTF{Alb3r7_OcB7RI4DKe_B3rn4rd}'), ('yRZhro8Z6RXzeTKV6BdZ', 'DH9kCzNpBU', 'QCTF{Alb3r7_ZZlreIXuqu_B3rn4rd}'), ('eY0v79HTfWX6o01FEvYd', 'OiYN9S4wC6', 'QCTF{Alb3r7_n5MQz0LOPm_B3rn4rd}'), ('OqOrVqVJsvtQ7OjfQJd4', 't24h9aZjQ6', 'QCTF{Alb3r7_Q5psivUFfu_B3rn4rd}'), ('T7iSgFkGcdtGs3tjoQMi', '2cERNSosAm', 'QCTF{Alb3r7_5YY036fWEP_B3rn4rd}'), ('4m5Sa9VnOHcswiX4EO8z', 'A1Yk2IUxAI', 'QCTF{Alb3r7_q80pAE6ACl_B3rn4rd}'), ('mmkaxk5wotbZ8PRA4W8l', 'lF9tVKrGnM', 'QCTF{Alb3r7_0WYmbfetPV_B3rn4rd}'), ('EfduBgwlW87nC7daVbLX', 'EMG6CiXWFv', 'QCTF{Alb3r7_mPsjHHsUlT_B3rn4rd}'), ('c0PtbnJh23pxtrHGwvy2', 'fKxwoJk4ru', 'QCTF{Alb3r7_vLtv0jgRag_B3rn4rd}'), ('Dp8yfNfoxX1a3T2dEYt5', 'qDF5n8GwNi', 'QCTF{Alb3r7_h06etIoPg6_B3rn4rd}'), ('j0ZW1Btr3psW62TFTVGr', 'kf9qZCxluM', 'QCTF{Alb3r7_xNPlpP5uNy_B3rn4rd}'), ('6OloMNA7dgfCWL0pvBU7', 'MSgqAeYAek', 'QCTF{Alb3r7_lQvu0cImMa_B3rn4rd}'), ('u2CAwtO49ssXjGBBxU89', 'oj5NxyJnE1', 'QCTF{Alb3r7_57kJxLIarE_B3rn4rd}'), ('Gvrh7TtEhankE5rwWb1L', 'j8UzcDZN26', 'QCTF{Alb3r7_dEfDIuVvX2_B3rn4rd}'), ('oK0J2XTg2SrNVSpkoxrJ', 'mIQHKInD0g', 'QCTF{Alb3r7_m5W5T6Wt9u_B3rn4rd}'), ('loylIOEZHZgUnLBxVYx4', 'MQpdA6j8uB', 'QCTF{Alb3r7_nxjo9bKCst_B3rn4rd}'), ('atmba6npRDuWwKGf7QIQ', 'rP8rmu99Xq', 'QCTF{Alb3r7_sossxmG2v7_B3rn4rd}'), ('jxWTVgudx3bLycWMlINA', 'CFu67yCgJY', 'QCTF{Alb3r7_mA07LjFhjT_B3rn4rd}'), ('uoeDqfwaw3VQiUdWkh8p', 'yJZk3Prtpk', 'QCTF{Alb3r7_Vf0TnjXhrq_B3rn4rd}'), ('oulohS48Pjzjpdv7h4EU', '3M9eABnuHh', 'QCTF{Alb3r7_Gk1PsQToQa_B3rn4rd}'), ('LmuCrnOs1M6LYREtj6zb', '6vu4ayMPHT', 'QCTF{Alb3r7_0NSrDrZPCT_B3rn4rd}'), ('nl7E82ztuUZaNK0Jaxfd', 'jdWPTPSdMD', 'QCTF{Alb3r7_iPzD2NBOii_B3rn4rd}'), ('rpzDAWydUPufcDqOPBeh', 'TEclMx0yDb', 'QCTF{Alb3r7_uNCossAnBV_B3rn4rd}'), ('wnZAnOMJ7mnojhmqjtNq', 'rtxSNjogpz', 'QCTF{Alb3r7_HaTBrHC73C_B3rn4rd}'), ('4CKtTy6cKJUZSmnRhOQP', 'anCtA7IeyJ', 'QCTF{Alb3r7_nYh8yta7xQ_B3rn4rd}'), ('WvHB52puHWKTl4czcOfs', 'mwOIu95C4g', 'QCTF{Alb3r7_jvgFRu0SMz_B3rn4rd}'), ('VXELCcZ8kMHc0dyXJG9m', 'gkjZhhPqM5', 'QCTF{Alb3r7_wbQIK9Qn0r_B3rn4rd}'), ('QpUF6poS4py7QKclNdQy', 'I8eOlYcOYI', 'QCTF{Alb3r7_qxCbP1R2VA_B3rn4rd}'), ('El48Kb96GmuiAqNeZWSX', 'gQ0JuJ6k4S', 'QCTF{Alb3r7_3Km5qkWHuw_B3rn4rd}'), ('1rq0q7yl2JlKRvkA7q5V', '0vLnqz7p7z', 'QCTF{Alb3r7_KVfxvSr1Vz_B3rn4rd}'), ('1eq123zi363jHQfqxdOW', 'D6sJj7iWfQ', 'QCTF{Alb3r7_DCu5xmajHx_B3rn4rd}'), ('d32mygUKZtGgYKw8sRCP', 'fjkh62LrBR', 'QCTF{Alb3r7_iF4VEVOwcL_B3rn4rd}'), ('DGxiJT87OiAwaF7IYolP', 'DbzptluhOg', 'QCTF{Alb3r7_3ggnBSnxZP_B3rn4rd}'), ('nHUFuDgo1Tdjjvl9mv78', 'TWEWS5E3wF', 'QCTF{Alb3r7_Vw18cH12lZ_B3rn4rd}'), ('GwMgzxBNqGj62HAsUDSb', 'h3MZBtSxKS', 'QCTF{Alb3r7_ThkKrXH70A_B3rn4rd}'), ('kwKJost0dY4vdGwvQn9t', 'sRGdv7yozq', 'QCTF{Alb3r7_OYdqwgNSVn_B3rn4rd}'), ('NTl5MGCkvELFcXPcn2yI', '0wKVMT0GVe', 'QCTF{Alb3r7_VjA2EDV9r9_B3rn4rd}'), ('27WcKbehxIDxjxYKUMPz', '6vLtoic966', 'QCTF{Alb3r7_ZvBD84GMmc_B3rn4rd}'), ('lH1ogfjoMdbZxN1zZiWv', 'jDLmfwugdD', 'QCTF{Alb3r7_6lSxP4cIjr_B3rn4rd}'), ('z7tpLPoZ7Wf2JQFMmtoa', 'Qk8XzkYUAs', 'QCTF{Alb3r7_N4uVKR9DrY_B3rn4rd}'), ('bduBASiUzc7e9OO3gphn', 'xGgOdId2MH', 'QCTF{Alb3r7_5kp1Bm0fMA_B3rn4rd}'), ('UapEtKeMIRCUqlLTZdgB', 'CtVJR63BSn', 'QCTF{Alb3r7_DWjAkA6D2R_B3rn4rd}'), ('6yLUKMPVJw8viiM72zO6', 'vZ8GuSJ1FX', 'QCTF{Alb3r7_p5gHEwfC3W_B3rn4rd}'), ('VKWaf54X7Ij7tSIwgAS7', 'EQPeRV3wbr', 'QCTF{Alb3r7_EXKSwTj5GJ_B3rn4rd}'), ('EXWXtyHiFRnQqLlywL4P', 'cqp3wH8GRO', 'QCTF{Alb3r7_dYaFhzBdHk_B3rn4rd}'), ('dP885nRtK5ClCUSyOw4S', 'EoEDZYSd7r', 'QCTF{Alb3r7_yrYv5nVLEC_B3rn4rd}'), ('Jb1FTD0Bpnrx4IN3Rl8b', '7KsHsjbwvy', 'QCTF{Alb3r7_03YOfPLrgk_B3rn4rd}'), ('3hKPASbKXGZVblSyRg3a', 'qN4Iuihy9q', 'QCTF{Alb3r7_xKV2ZhPA6P_B3rn4rd}'), ('3Qlq5bHoo7fRzWNjDaOb', 'W4HSST0Ldd', 'QCTF{Alb3r7_QG5ZvRMfsV_B3rn4rd}'), ('r3QYGAADkf6mlKRtIXHT', 'qkmt4hpEzn', 'QCTF{Alb3r7_6DDtICsfFg_B3rn4rd}'), ('0odNHJXEfxXg3SylDyPs', 'OGrye86jgh', 'QCTF{Alb3r7_2yPy1kW3WT_B3rn4rd}'), ('cgw53tydCrpNnthpOAs3', 'QCuOaA84fo', 'QCTF{Alb3r7_8gnRHE6vlJ_B3rn4rd}'), ('wO9OyyEzOV2N2LaxMjCj', 'twXqHf8VaJ', 'QCTF{Alb3r7_cI4Grd9ZDa_B3rn4rd}'), ('DoffuBLYziL2jnkK7wRn', 'hzZQINmuea', 'QCTF{Alb3r7_UpX4X7Fuo7_B3rn4rd}'), ('O2H2Reosm2C7LhxxFFgf', 'iV0L1jobkI', 'QCTF{Alb3r7_VFBtYwcQpz_B3rn4rd}'), ('QA9sbNhoTrT1JF951Jkz', 'upojY2yOpl', 'QCTF{Alb3r7_7sytxi4NyJ_B3rn4rd}'), ('hmBndhlobfflKgLUDkh3', 'ri4FnDlHFx', 'QCTF{Alb3r7_ECvFZErayc_B3rn4rd}'), ('PVmqfTDrmQuSHOqmntv1', 'wC6VKfRWPc', 'QCTF{Alb3r7_pKlHLbtEkV_B3rn4rd}'), ('xVLo9pGKhWR5fL9Pet1v', 'AeZ7hu1Pcz', 'QCTF{Alb3r7_j3HQRUNbRg_B3rn4rd}'), ('5Oky9d9izqH8dlDc2JIF', 'eDbhCTHFTT', 'QCTF{Alb3r7_AlSpxYqa6O_B3rn4rd}'), ('Jebkx2vsP1hrHlokwWAl', 'WWrUeqWQNb', 'QCTF{Alb3r7_5HdzcOURe0_B3rn4rd}'), ('RKuGZJirhKV5UH2P1lkO', 'chNoD1Qwbz', 'QCTF{Alb3r7_npjVu06om1_B3rn4rd}'), ('ITtENsn1MQb40M0vr7TO', 'jIs9bAIgUF', 'QCTF{Alb3r7_VNbhRqJWit_B3rn4rd}'), ('fmkeUA5zaiRDSxQWHN2v', 'sJSzUxbExx', 'QCTF{Alb3r7_08Ogcingmr_B3rn4rd}'), ('2ZjvPaMSfMukZffLjCx4', 'zaFpQeOxOP', 'QCTF{Alb3r7_cNUST6VSa2_B3rn4rd}'), ('W8sahkEbqzVs3noNQOJt', 'qjZCmjACWL', 'QCTF{Alb3r7_lf3uHhaH9r_B3rn4rd}'), ('7w85FrQMBx8zGuZonnQf', '7ESrwSIBVT', 'QCTF{Alb3r7_UPfklFZAIq_B3rn4rd}'), ('5ax2iH5h4T8B7xDd6pBT', 'WGzQsQtHtB', 'QCTF{Alb3r7_l76Z00RVOK_B3rn4rd}'), ('nleZXsu9y00qgpw7wgCT', 'VItp54BhNU', 'QCTF{Alb3r7_uZdSq6Uupu_B3rn4rd}'), ('qO3GMXA7UqWLsaTkXFHX', 'SWf3l7r6W6', 'QCTF{Alb3r7_CWtjUZVIjl_B3rn4rd}'), ('k3Wbs7dBjYd9cJ95nQtf', 'cujB6MYv5y', 'QCTF{Alb3r7_7aF7bYsyva_B3rn4rd}'), ('CG9deSNhuu0nmNcygDRV', '3aYQ10Wz8X', 'QCTF{Alb3r7_wNVgbagoWW_B3rn4rd}'), ('a3qrzWt6TiBU08imn4I7', 'CBjcAAoezy', 'QCTF{Alb3r7_fLV0xuTUKZ_B3rn4rd}'), ('LbFVKW4UKpDMjSWl6XXk', 'wZGV5vpvAR', 'QCTF{Alb3r7_1ga4KQuD7p_B3rn4rd}'), ('orFsPsoYalNv3FwEXmE0', 'qmU3wDBEpI', 'QCTF{Alb3r7_7GFPO3GWNJ_B3rn4rd}'), ('aHmJhrOnFMZO4cx7ENB8', '6bVpfOVFkU', 'QCTF{Alb3r7_UrvUN2O6Wc_B3rn4rd}'), ('6kiiaZF1ahimc0nPWrwZ', 'K4YjfjQh4T', 'QCTF{Alb3r7_YOsXK2oyqB_B3rn4rd}'), ('xnvtN658d1Urvh9RDLhn', 'IS4Ef2epNN', 'QCTF{Alb3r7_z5b4DLljfe_B3rn4rd}'), ('zXChhN38GTcdfnSzXnD6', 'fSQFjeAin8', 'QCTF{Alb3r7_ROkXJVAnZK_B3rn4rd}'), ('3AScHpcAYyNCFmtZiMmj', 'nPhogd5Qvn', 'QCTF{Alb3r7_qlM6RW7DEu_B3rn4rd}'), ('6arZXtIGrKrv7vktqMC4', 'TGjMxyL4E7', 'QCTF{Alb3r7_rMvVgNCWrP_B3rn4rd}'), ('2KGPEbS5RGAM6aQ7Nt61', 'a2Cr3XIWH4', 'QCTF{Alb3r7_ibnBPhtjCU_B3rn4rd}'), ('wSR1hazcHI7KrSqrBdGr', 'MWEh60wCB8', 'QCTF{Alb3r7_qpKSDFqIWQ_B3rn4rd}'), ('qbI5Gs9Eae7i8QpW58DM', 'OaZSSnbcqp', 'QCTF{Alb3r7_useF7ernRL_B3rn4rd}'), ('o5Lz2d6KE34Ur1ELm3GJ', 'hMU1vnJkWp', 'QCTF{Alb3r7_g4ZHXpa0yw_B3rn4rd}'), ('l1d0z7HDfNY09hRx43zu', 'dqFvsgtB6D', 'QCTF{Alb3r7_iFCEwoznmf_B3rn4rd}'), ('98TvCXhbm1U25Zw4pi31', 'jGbsyuCwc2', 'QCTF{Alb3r7_d8jNUCaMU2_B3rn4rd}'), ('ib80zc8Gxod3LNrallNP', 'qQlLPYU5lH', 'QCTF{Alb3r7_HlZjRtk7YW_B3rn4rd}'), ('iDk6HWTWyzXGSXqGYxup', '6UP9XDWDLR', 'QCTF{Alb3r7_FD61DHrWhy_B3rn4rd}'), ('VAzjziGMI9ZTQHiiwqgo', 'iLJ4RS6Kp3', 'QCTF{Alb3r7_KNnTya2e66_B3rn4rd}'), ('LyBLSTOGTaOlCTBS8jIH', '9yFvLv387L', 'QCTF{Alb3r7_bhunn2L2Iy_B3rn4rd}'), ('AnXAA8i2gFTtS6rSxE0b', 'GiT1HNzA5J', 'QCTF{Alb3r7_HnhbeaysJ2_B3rn4rd}'), ('fClgOYtZavoRj8BRj7zU', '0lLwn0NU3e', 'QCTF{Alb3r7_ZCu35rmEgu_B3rn4rd}'), ('O8s9lbHv7lpGUpS8stUq', '4YpFjFAJlm', 'QCTF{Alb3r7_Pw8bLTYURb_B3rn4rd}'), ('6rAAxjyf9e88p0pAbQo0', 'eNGcrBXow5', 'QCTF{Alb3r7_pnKBz3rxP5_B3rn4rd}'), ('l2PpSHFtUvu64ggoHJNg', 'PV9vducKCS', 'QCTF{Alb3r7_v05jkxl4sa_B3rn4rd}'), ('D1OSzlda7ATsoA50Pixt', 'yh0LmO2x30', 'QCTF{Alb3r7_xsGg0XiAa1_B3rn4rd}'), ('OidS8h0bQtg7ahwOrxV5', 't9ViEHh5rK', 'QCTF{Alb3r7_1U2Clqr1W7_B3rn4rd}'), ('EvXBM6lDWDCpScszEIH6', 'i63BtudHjX', 'QCTF{Alb3r7_sGtGq8YlJl_B3rn4rd}'), ('uqIsAq84qBmRSeIUBWu9', 'zZ3N1dDQmr', 'QCTF{Alb3r7_PS3PoL6SQs_B3rn4rd}'), ('hseP1bwcgcPdBhVXJSAU', 'noz0LrVdId', 'QCTF{Alb3r7_lIlCB1LhCz_B3rn4rd}'), ('Jjv2GFcIMm6xXO7PwpgX', 'vAMT8SKRL7', 'QCTF{Alb3r7_MQiSAhoXyA_B3rn4rd}'), ('n8VUTARAkAnwWXI1z8XV', 'g1ajXLfHp1', 'QCTF{Alb3r7_x81ZYFtY9L_B3rn4rd}'), ('2uyAVP8VrLvvnjST6s22', 'DImUa9KSCL', 'QCTF{Alb3r7_C9O4IHDPNo_B3rn4rd}'), ('UEEe6HHXE7tt3h9RDevD', 'Xl60A5RWOq', 'QCTF{Alb3r7_or8xECdJSO_B3rn4rd}'), ('CEUc5xTXwdE3i61WW4po', 'tWm2O3PKJH', 'QCTF{Alb3r7_Mg3mwUKL7f_B3rn4rd}'), ('OV4Ir2KNhgjpGkDyWNvd', 'khLQeiCh0N', 'QCTF{Alb3r7_p5YNmWJOuO_B3rn4rd}'), ('CDTcoUj5lyW1Lr0gyeak', 'SY69BX48wh', 'QCTF{Alb3r7_sYNYmvYej4_B3rn4rd}'), ('A2PyrrKf9zzPo5y4YhJs', 'Cq0VNHcNld', 'QCTF{Alb3r7_aeAdFeAIb7_B3rn4rd}'), ('wteYjxWZWneCR9aH3zns', 'Z1Ie0Hsybe', 'QCTF{Alb3r7_L3aQ7HnztQ_B3rn4rd}'), ('lp2X0K5ZDHdevU5WANTZ', 'ua3k86T29Y', 'QCTF{Alb3r7_Cy9A0kqWgs_B3rn4rd}'), ('mUvlF8jGDWscZIXv2zyO', 'oMvliYU45Q', 'QCTF{Alb3r7_gnufvdBNWO_B3rn4rd}'), ('JSBywgYeCvLt8ZJmf1Xn', 'gN1Isa9NXi', 'QCTF{Alb3r7_NJW4XXcSHg_B3rn4rd}'), ('YhprYDV69vdxgqceYAdt', '9oSOpo0tfv', 'QCTF{Alb3r7_H37Gh1UHtF_B3rn4rd}'), ('UXakanaFW90ptXFQcfDS', 'u3LhuSUilc', 'QCTF{Alb3r7_WS2wsyWRXA_B3rn4rd}'), ('X75LEqPjNeoyCcCeW5A3', 'raOS4geqeb', 'QCTF{Alb3r7_6iYKjdVw9g_B3rn4rd}'), ('313TP7yKYkUUE0RoI7TO', '5lsIM5OlvE', 'QCTF{Alb3r7_cQIqLHE12V_B3rn4rd}'), ('wbqtNWPJOeDCRzfJKvCs', 'HVpvY6M2k3', 'QCTF{Alb3r7_7MDHTPUZWN_B3rn4rd}'), ('isNWRu7bAJrdCsCvm0gs', 'rU2uFAgVaP', 'QCTF{Alb3r7_lMhbTWbFuu_B3rn4rd}'), ('hF6TYQu8HFS45J14OUQZ', 'KvsTjRWMN4', 'QCTF{Alb3r7_ksw9YMfbsR_B3rn4rd}'), ('VABUZEusIYnNkiVLHxbI', 'MyzlvqvMvq', 'QCTF{Alb3r7_R5SJPU4lWX_B3rn4rd}'), ('mDEII7TJwsZXG49DEiYa', 'by4EduxOxq', 'QCTF{Alb3r7_OODvIgoqpO_B3rn4rd}'), ('jogcantkx2AidmFTHD6S', 'UuAfnCVjcR', 'QCTF{Alb3r7_QDAhQzy1pn_B3rn4rd}'), ('CBtVFZdJ4waXBh9co9Sc', 'iprxg1jwt6', 'QCTF{Alb3r7_NxtxDRaKcc_B3rn4rd}'), ('NmIXa4Ss1xHBiowz7grr', 'pcLzJ6NgLm', 'QCTF{Alb3r7_QLO9WfyrxX_B3rn4rd}'), ('UDuAElmRY1kL2MfG0pnj', 'TugUyiJiUA', 'QCTF{Alb3r7_X1a3qJzG2h_B3rn4rd}'), ('r53k00aIFSwxxEzj4LTb', 'ZhFDoVRvso', 'QCTF{Alb3r7_N2bQbgWwYz_B3rn4rd}'), ('h6BdnaSwDSuHUW02t1i2', '0UJYPVjE2y', 'QCTF{Alb3r7_tuqnZoUYk9_B3rn4rd}'), ('FrJxapplELcjSlNRLhhY', 'OdZQR0spE8', 'QCTF{Alb3r7_DmzP6eaeV2_B3rn4rd}'), ('txyjKTJUesEKtOZsqLpM', 'qQgcizVBht', 'QCTF{Alb3r7_oRfppceDFm_B3rn4rd}'), ('rYEXlAZqgYMSsm3pPELP', 'THnL9hewY1', 'QCTF{Alb3r7_6Uco4KEmNA_B3rn4rd}'), ('8UgES7XdMvwjXI3Ltf9p', 'LyocqpyIdq', 'QCTF{Alb3r7_0XhGWxcYrm_B3rn4rd}'), ('CMqOdTEaOoOg5DhGYUV4', '15NPxdAntI', 'QCTF{Alb3r7_rjlzDYNqqp_B3rn4rd}'), ('8LkELNde3OxWVAETdxbe', 'OSlHXbkFtU', 'QCTF{Alb3r7_vj6c1WZG7J_B3rn4rd}'), ('klWJYNEgaSxJceCBiVzA', 'Oy78u5Y2sW', 'QCTF{Alb3r7_DlUQjVlgSG_B3rn4rd}'), ('dloZGdagmZ5ThIbfko2b', 'cQkeAFlnll', 'QCTF{Alb3r7_db7odn0Bhr_B3rn4rd}'), ('xqHUz4qLZRny0YPzqkmR', 'zRSqLsr3p6', 'QCTF{Alb3r7_f2bIG0JeYS_B3rn4rd}'), ('gWYVVlYg1efIaSn2LZsm', 'qggYYs5fWk', 'QCTF{Alb3r7_oiMABv4Hx6_B3rn4rd}'), ('lFRYTv584W8mBaYHqzaY', '6h0tlBuz15', 'QCTF{Alb3r7_l4fOPxhURy_B3rn4rd}'), ('I7ijNcQh3diTNSu8VhzV', 'a6XSFCuBMX', 'QCTF{Alb3r7_qViFITOjUo_B3rn4rd}'), ('shuHHbCdtYa0hkIzcIe8', 'mDE5sdfUSI', 'QCTF{Alb3r7_OEcVROvLXm_B3rn4rd}'), ('3Y987KGpTg5rHJXDDscO', 'dnJTwzXyxu', 'QCTF{Alb3r7_RjU6sBmnIg_B3rn4rd}'), ('nlo6NMgVYv4OWwnXFKB5', 'GKJo5c5H4f', 'QCTF{Alb3r7_MoR10hj03b_B3rn4rd}'), ('PEOKtEYM09EKkEZOfldk', '9bvTK9sgVE', 'QCTF{Alb3r7_otT4pn21iV_B3rn4rd}'), ('8fXW1Nqz4grsVl6UmGlB', '61e78TjlVn', 'QCTF{Alb3r7_BKC5GirTGP_B3rn4rd}'), ('1q5ADt9Ueij57DceCRUq', 'C4Jzii4W4y', 'QCTF{Alb3r7_QxAICvFEzT_B3rn4rd}'), ('9uw5yD6PVdBrFcvamw1M', 'Lanrhr2eST', 'QCTF{Alb3r7_WtU5Ts0P0i_B3rn4rd}'), ('ob4Gt6OMhoBurFz8X4BO', 'cqhwn3ASF4', 'QCTF{Alb3r7_WhyutMgWdI_B3rn4rd}'), ('NB0Nm14fn5quhv0abtci', 'DbohnJIuNv', 'QCTF{Alb3r7_0pYJgi4jwo_B3rn4rd}'), ('FvJcZMLPnDJiGd2mxUo8', 'XQO7f3Uab7', 'QCTF{Alb3r7_mYAHmPSRte_B3rn4rd}'), ('6Nxg7ZkKwI2ymPrNAQrU', 'X88I3ilyBL', 'QCTF{Alb3r7_tbQR8HbZxg_B3rn4rd}'), ('J21GPTt3U2dd3bAxg60i', 'FLf4lcVFUO', 'QCTF{Alb3r7_gKnfHAGgzT_B3rn4rd}'), ('CyaRYQr4r9Kyc6Irqj9W', 'mBqduRtV0S', 'QCTF{Alb3r7_aHUV4QlD9Z_B3rn4rd}'), ('se639BULNBEZJxaRHeC5', 'lpZBkpOzqU', 'QCTF{Alb3r7_PWaDIwdUT9_B3rn4rd}'), ('pvMf0ch8blMmOHAsL2mF', 'oGYEvzqQSb', 'QCTF{Alb3r7_nRTq6TvnPT_B3rn4rd}'), ('X4zVOcHOlEDQZJ8Ss7Nc', 'T8J5y2Wp4W', 'QCTF{Alb3r7_KqnSV4XjuC_B3rn4rd}'), ('JaCT4096ZtJp38O9NSIn', 'SPS5Ps00Ob', 'QCTF{Alb3r7_yu8YaAsFqm_B3rn4rd}'), ('EO8jPDIQK5aPfoUdeMlA', 'LA23A7rJy8', 'QCTF{Alb3r7_CZXGKtpfXz_B3rn4rd}'), ('cGuoNCKKjMphJKyAnIgu', 'xPFoT9jM2x', 'QCTF{Alb3r7_2MEDCd6wrz_B3rn4rd}'), ('80rRDsW0f0S7YhQnusr2', 'YB9LuHxwjT', 'QCTF{Alb3r7_Lvo0vSHoV5_B3rn4rd}'), ('x3Z0O3DmRxh5YvfcWPtS', 'ZuNQqF96qN', 'QCTF{Alb3r7_HxC4XLrHqQ_B3rn4rd}'), ('QzcWRTOCZ10SByhfHmGu', 'MfC2pJdnKQ', 'QCTF{Alb3r7_cBNqgsdClg_B3rn4rd}'), ('uxuLuvIpXxzWzkg14JVP', 'ESneLjfhKp', 'QCTF{Alb3r7_Jlp4iT7N6u_B3rn4rd}'), ('pLqIOqXq4rrNNkW23Ycd', 'Xh7QVn4XUt', 'QCTF{Alb3r7_RPYOo1iRHV_B3rn4rd}'), ('dPvwUD1YrFfZpVbgV6lb', 'IFn2f8rxWH', 'QCTF{Alb3r7_mEPmEKqen4_B3rn4rd}'), ('7ZXyRVWtXFifUWAfEEtj', '5GdSn5OzWu', 'QCTF{Alb3r7_UfUzbI59Rk_B3rn4rd}'), ('YJ4q0I3c8l7RQ4REOxJK', 'cvW28u4kDS', 'QCTF{Alb3r7_YiVQBF92sR_B3rn4rd}'), ('rKeQxu6zAsthyZmmmC6w', '0SA2pYUR29', 'QCTF{Alb3r7_5kNqx3FFMP_B3rn4rd}'), ('r6B6Ag9go8onBSX93EZx', 'tJ9jdIV56A', 'QCTF{Alb3r7_rMNqohtZyj_B3rn4rd}'), ('WSv1oCE8mb4GUc8zLrVk', 'aEeRaNGTj9', 'QCTF{Alb3r7_g6LPNekD73_B3rn4rd}'), ('ofbQZ9saegoO4nyi5BwY', 'rFdzgrruJH', 'QCTF{Alb3r7_4xAhfDMk16_B3rn4rd}'), ('cyEaRuAIC4Z6uoMi9ExB', 'sqTOec4CN1', 'QCTF{Alb3r7_dpwDMsPFMN_B3rn4rd}'), ('i755jgrEsGi9GJCFtjd6', 'UztKnl16Vj', 'QCTF{Alb3r7_QCx7v5GjqZ_B3rn4rd}'), ('sGAuW7igkUHhjdxkTdJC', 'EdB0FLxOAf', 'QCTF{Alb3r7_J6SjOwhKCJ_B3rn4rd}'), ('t6AvPY6sY74anVVUrO4c', 'eqIn7ZiGpd', 'QCTF{Alb3r7_E7Oz8Ao01x_B3rn4rd}'), ('W4RjB0GndxJBcnbgO8vz', 'rvQZkgxpKt', 'QCTF{Alb3r7_CTVAqFIXLr_B3rn4rd}'), ('gW9FJfGFYXxlU3PPkrks', 'dvS8pX2ElP', 'QCTF{Alb3r7_MHusmp8na3_B3rn4rd}'), ('gEfWUb2WBQtAwXlksmda', 'ckkVM9QrPI', 'QCTF{Alb3r7_FrCEUimqsn_B3rn4rd}'), ('PVAXVmBS3cJPSJ2dgAwi', 'Comu8JGfmv', 'QCTF{Alb3r7_h8fg0jN7cA_B3rn4rd}'), ('BTNsemVt6KvoKjdeQiPp', '0ZLp8BnhXS', 'QCTF{Alb3r7_ydltVtUvtF_B3rn4rd}'), ('JQVXlvSsU9ylAxV1DCxx', 'j2b1sPZg0M', 'QCTF{Alb3r7_uJic1ZLzsi_B3rn4rd}'), ('0bU7CdSknl3ZE0AQesFq', 'uBxOMAU6yY', 'QCTF{Alb3r7_nmVGi6B1SS_B3rn4rd}'), ('wyYIbDpHr8bgVIpSEo8T', 'KrwLwcxt8j', 'QCTF{Alb3r7_HMnlJXfxbV_B3rn4rd}'), ('RTCpxXyar2yO3QS4jcmo', 'SNUJfNZCKD', 'QCTF{Alb3r7_GX3OBT7Cp3_B3rn4rd}'), ('g81xfQ973oPGZzv054vp', 'AhltrA5rr8', 'QCTF{Alb3r7_SfqiKZr8Ll_B3rn4rd}'), ('Gab8RQe7SIS1wEa30mYz', '0tgJWyG7PB', 'QCTF{Alb3r7_rcaI1YTA3V_B3rn4rd}'), ('Meg0r3iycGceJFCYXglh', 'cdyzwwNFVw', 'QCTF{Alb3r7_0pTg67wJRb_B3rn4rd}'), ('3MvXZ8ZgBotCxcrvLTAY', 'h1StOMT8ui', 'QCTF{Alb3r7_Sj5iBa8ADr_B3rn4rd}'), ('EmslewCeFFo3W2AU3gqI', 'wbji3omWu0', 'QCTF{Alb3r7_xbvNCs0Sas_B3rn4rd}'), ('y0uFAjI0bRhoJofNxhev', 'gi3b6iEyBe', 'QCTF{Alb3r7_WnyelVVW3o_B3rn4rd}'), ('8tDGuQsrKIC6YnHN7Mbi', 'M3ekpWrnB0', 'QCTF{Alb3r7_czr5Na15Ce_B3rn4rd}'), ('UbV892SZP5q3YGHnkgSC', 'Kvyzg9nM4f', 'QCTF{Alb3r7_VocvgJqx1A_B3rn4rd}'), ('pWYFxsD87lc3aNqOWD8e', 'sjhl2ZPKaN', 'QCTF{Alb3r7_i21FkDRMdl_B3rn4rd}'), ('gVcOL1shCEZ7aNip8Lxw', '3opw6aEFrD', 'QCTF{Alb3r7_2oEH4KSqhO_B3rn4rd}'), ('HwR9YX4AI23ibf4hGeQ9', 'dg25WmBlpc', 'QCTF{Alb3r7_J8z43cbLqt_B3rn4rd}'), ('Tc9I4f0N9whe3vFxBYOO', 'eGKTZtG4oh', 'QCTF{Alb3r7_0Kto7PEmMg_B3rn4rd}'), ('VPmeEELxO6Thg3EF021G', 'CKsYDfvNlz', 'QCTF{Alb3r7_ReWRlhUVww_B3rn4rd}'), ('ZiOfgk4N6HsqOnGawTc1', 'sv3JBO6pVQ', 'QCTF{Alb3r7_8vAfrz3g4K_B3rn4rd}'), ('NSgUK3jlGRMiKdkmx9WE', 'J55wWVivjE', 'QCTF{Alb3r7_EvfVU64thn_B3rn4rd}'), ('LXOmcTWx4XScoY6VXBZe', 'BWVMy12G6O', 'QCTF{Alb3r7_jcfJa2gH3B_B3rn4rd}'), ('Ur2TNwGKByUZyHDDh0bz', 'WfTmsgfQhr', 'QCTF{Alb3r7_tfg9JsMCbe_B3rn4rd}'), ('i6C0FBapxzzQqeOTPbvq', 'rhTgmPWhsR', 'QCTF{Alb3r7_qCbxcfKrBN_B3rn4rd}'), ('1PV0KB3JchXf1nnfeOwK', 'OnQLW3uVBx', 'QCTF{Alb3r7_SGlESjOccj_B3rn4rd}'), ('j3XHuS2YqAJctZ964tBq', 'BTwqB6vDIZ', 'QCTF{Alb3r7_TJSoGkLSaC_B3rn4rd}'), ('rx49DYYSaXJQV266AgSn', 'oC60gsRamE', 'QCTF{Alb3r7_EM5OMorSSL_B3rn4rd}'), ('wGmDHGt5XWUC8s8MsbT0', 'SKOGVJaGic', 'QCTF{Alb3r7_mMNy7QM1PN_B3rn4rd}'), ('7qDn2QeQ8jvo3hCAc2kW', 'RMLOsl0Wuq', 'QCTF{Alb3r7_4P5boqXAig_B3rn4rd}'), ('h28s0nccoW4iFLyqxZDh', 'ONcFIGM8Ol', 'QCTF{Alb3r7_eh0TU4ZZYJ_B3rn4rd}'), ('PsaxA1D0JDqoEZaUoZLi', 'XZdQRLfrvJ', 'QCTF{Alb3r7_NidWlBvNCw_B3rn4rd}'), ('gJOXM1hdFkGQcL5ifFdF', 'HFBvNpFaiq', 'QCTF{Alb3r7_sCzO24nD5M_B3rn4rd}'), ('uNOZRfSrpRfjXLSqDXOZ', 'g4Yu3x3sMr', 'QCTF{Alb3r7_Se2Ar5PGlA_B3rn4rd}'), ('hrou6VUfSKCZEpG2NQ1k', 'SOVCB2YYY5', 'QCTF{Alb3r7_JX5lqIqCt7_B3rn4rd}'), ('YzZQwBYaVcC43pkTh3gB', 'YczHEa8pnq', 'QCTF{Alb3r7_CfdEdYMUtY_B3rn4rd}'), ('tqnlul8UmkVyIoR0RXvR', 'HeiIDxnnet', 'QCTF{Alb3r7_KZ5bquBAM2_B3rn4rd}'), ('Kyq7blqbFXAQDwGogwNc', 'IiktAxiYYS', 'QCTF{Alb3r7_U2vlIalixV_B3rn4rd}'), ('dMkyEeehve62CmaSpowz', 'ytSI1v8W6B', 'QCTF{Alb3r7_lYoP1Ia365_B3rn4rd}'), ('WBWbHBYLcK2inMsUYkVL', 'RLmH0aaQry', 'QCTF{Alb3r7_tjW1hCpsRc_B3rn4rd}'), ('7dp4oqgjvT2GxYWla1x6', 'R9XH4b2hIE', 'QCTF{Alb3r7_4Hq1bLS3A6_B3rn4rd}'), ('Meb3UwqNq5PKQPQPDy3t', 'l9i2uPW4Qt', 'QCTF{Alb3r7_jijpF4M6qG_B3rn4rd}'), ('EsSLm8IHqLMGtX0c6ePy', 'xMYZNalbPM', 'QCTF{Alb3r7_fdxewa5kkE_B3rn4rd}'), ('Thzn7r3Uu0LVp91LlzKp', 'InBqD6alcE', 'QCTF{Alb3r7_grtPr7SEsP_B3rn4rd}'), ('ePZkcO414LmAhrkG91Cj', 'TeT2zkd22j', 'QCTF{Alb3r7_nqnXrUF0X7_B3rn4rd}'), ('tPaN3QUSHb2H7kAvK9yA', 'w0Qr6hxxs4', 'QCTF{Alb3r7_r8FHUhyYtw_B3rn4rd}'), ('T4Ygd0UPkyvjJcp1HU6d', 'f6KwVO9Dnk', 'QCTF{Alb3r7_bDdUeHg5lZ_B3rn4rd}'), ('LucNrFkTb2aVVtFVQUbF', 'ywcgcNMvT7', 'QCTF{Alb3r7_EX8GzBvCDz_B3rn4rd}'), ('AVwlpwSBrWU5pC9ADWgT', 'KTvLR3xawJ', 'QCTF{Alb3r7_0jGcOuNmUE_B3rn4rd}'), ('3jE8B4ZsFYlJX46AUydp', 'kCO1bHmZo4', 'QCTF{Alb3r7_OcxjKgIiLm_B3rn4rd}'), ('WVYiYuiNW6PDrTHktUyy', 'Ij2PNIoJZY', 'QCTF{Alb3r7_O672QPvxck_B3rn4rd}'), ('m7LoABbpDf2brnFqWnRZ', 'jySm2RZ0EO', 'QCTF{Alb3r7_Df9UBaZ9U5_B3rn4rd}'), ('nTQqQM3j9crrjkhRAZ4h', 'RjV7IIi1zK', 'QCTF{Alb3r7_1cCEVuoRh7_B3rn4rd}'), ('AyGlJB6xAZOtAxMDYgS3', 'etBc3ZvTRo', 'QCTF{Alb3r7_cF37igtg8I_B3rn4rd}'), ('mpG7zfrVWYOXCEh5hyeg', 'JqQfFrEdqy', 'QCTF{Alb3r7_X4sOcGf6WX_B3rn4rd}'), ('McJzASrqxx4sI82T8N1p', '8dg7NE579r', 'QCTF{Alb3r7_OQBDLFdDOS_B3rn4rd}'), ('GpK9FncVjPmalgV8FoVg', 'EkNl8akNhm', 'QCTF{Alb3r7_BXuOTj5Jnc_B3rn4rd}'), ('1ub2O6OM7hS0WwvOvu62', 'rLUyyhghEL', 'QCTF{Alb3r7_Ew9FsEMKqf_B3rn4rd}'), ('EqAJnwxwAq7hVlXJRXYa', 'dFAiZbhxvC', 'QCTF{Alb3r7_buoBNZupNY_B3rn4rd}'), ('LAN17EjM4Owckj8YmiNt', 'Uu12ty85nG', 'QCTF{Alb3r7_ddh6OkY5Hf_B3rn4rd}'), ('IRsSggFM8siTPkhUw1rN', 'rtVCWWjCvC', 'QCTF{Alb3r7_9wooDpOmEB_B3rn4rd}'), ('Hd51rG2j7UIF29HaP0vA', 'SLHta3vkA7', 'QCTF{Alb3r7_D8byqjbj3K_B3rn4rd}'), ('kEtMCB4nEJhroo6r6fWX', '7eg5X149fK', 'QCTF{Alb3r7_gSSYET7p6v_B3rn4rd}'), ('DSdcop2sHywbM7wKrtxK', 'dJYuCXYuXB', 'QCTF{Alb3r7_kDdmh1jOSy_B3rn4rd}'), ('g1opAULrMWArcOgQKgRR', 'rBz71PxDOH', 'QCTF{Alb3r7_bKjCs6FviF_B3rn4rd}'), ('8ztn2AhPcK56r2j70XsK', '9L5on3nmZc', 'QCTF{Alb3r7_m6vhEJOAGb_B3rn4rd}'), ('owTx1lSXqzSct5VGoUch', 'FwffCl7mJy', 'QCTF{Alb3r7_k67aLU0Tm5_B3rn4rd}'), ('hpWQSgZGhL4OJbZQfqJZ', 'F0O0bSmQLW', 'QCTF{Alb3r7_dxCS0y3hlJ_B3rn4rd}'), ('zahYc2SXnOJgNH1POLh5', 'fAyBmqvEvU', 'QCTF{Alb3r7_cX9IqkxcKD_B3rn4rd}'), ('kFCojHTZChaDIc8L4vzZ', 'Cy3xqiidPH', 'QCTF{Alb3r7_T0ckXcH27a_B3rn4rd}'), ('2qPKULcwUCBhbD0pV6xv', 'Fj9WIzQKGV', 'QCTF{Alb3r7_GYqBZNScpR_B3rn4rd}'), ('znQ6N70YZlnG0AqJjJXt', 'UqunonsjLp', 'QCTF{Alb3r7_1lW7KjozuR_B3rn4rd}'), ('4W6IoA5F8ZQcIpk1QPul', '2us3b49KDJ', 'QCTF{Alb3r7_j2LK4aEpyF_B3rn4rd}'), ('oAIfij8Xkg6P094a7dgj', 't8Z8vMgqOZ', 'QCTF{Alb3r7_MzT3ZQvNui_B3rn4rd}'), ('4jVZCEG5YP7JMXLRRvK7', 'B1F5o3VfcD', 'QCTF{Alb3r7_qRLMTBPJQM_B3rn4rd}'), ('yAkNw94KvxQ1H0T6RwIe', 'tl8vTS1pjk', 'QCTF{Alb3r7_3ilaQRfHLW_B3rn4rd}'), ('QNlnblY2UUxq5Wfo1uJn', 'hW18QKUqWI', 'QCTF{Alb3r7_4yZ5zlwdjl_B3rn4rd}'), ('v0NgbjvqNSZUHUzp5VrR', 'orCjWRJIZ9', 'QCTF{Alb3r7_F2UDVDfY3h_B3rn4rd}'), ('3NlAEFpClPyRI6OLFP6a', 'w0PM79B57L', 'QCTF{Alb3r7_S78XUGXSTr_B3rn4rd}'), ('jViPqX0eVCjJBbQiSxvu', 'liO9hVmGas', 'QCTF{Alb3r7_T0X7Saf8NR_B3rn4rd}'), ('B6xYaWY03OsOe4Ij9342', 'er7pnk6TJ0', 'QCTF{Alb3r7_BjXmG1m6Yi_B3rn4rd}'), ('mEL5ngREeQ7YrsrDyZyG', 'TvoNm1SMbD', 'QCTF{Alb3r7_r6vpLX8OE6_B3rn4rd}'), ('qikPo4lcGZQhYPmjTt2o', 'K19DTFzEKd', 'QCTF{Alb3r7_q4dfh4m65G_B3rn4rd}'), ('C97oHUhV8dGJmqfWJGfD', 'tyyOq58QM5', 'QCTF{Alb3r7_GhNUXckVAL_B3rn4rd}'), ('OzCeXqEfDVbCfCBz94c5', 'K8Sa6xkviZ', 'QCTF{Alb3r7_Vbattod8KF_B3rn4rd}'), ('Jo39EwyphVT3bVwcu2Ch', 'DdLDN5wQEN', 'QCTF{Alb3r7_ZyB98f6NNp_B3rn4rd}'), ('EAYs2DIQBzJm1ya6bHLY', '2QVfQFMxHL', 'QCTF{Alb3r7_x3d06Dppmp_B3rn4rd}'), ('KdA8EcS0GzocOYBvonpp', 'faC1TBoIu3', 'QCTF{Alb3r7_nbfpxe4xw2_B3rn4rd}'), ('pC5MPaWzJ80HTDXXI01X', 'hZpwG5yvua', 'QCTF{Alb3r7_CjAJEMoE4N_B3rn4rd}'), ('8gydnageAsDl2qLn5Xt1', 'WRkYot0ReR', 'QCTF{Alb3r7_bdZ6VDV459_B3rn4rd}'), ('orK3YK4CN1WRMc3QMq4G', '6dCCAB4oJW', 'QCTF{Alb3r7_HwtpDn0t9j_B3rn4rd}'), ('PCzrlS7Y4k585RZXlpFW', 'rpMret7SIs', 'QCTF{Alb3r7_NyzX6Mo3AY_B3rn4rd}'), ('Fjg5dLBImw7KoDBfIPbi', 'ngfhZnKLRW', 'QCTF{Alb3r7_RmDBN95w8J_B3rn4rd}'), ('s6sDFk4vPBUVcgqpepC2', 'yd69KbbWHb', 'QCTF{Alb3r7_0umPL06BtS_B3rn4rd}'), ('rUqs5GzHLikJGPQhOQiB', 'FF8idX2Uv9', 'QCTF{Alb3r7_Lyj7zWsWEH_B3rn4rd}'), ('4LmOm6xysQB5cNT97Iob', 'OXzwowaOlT', 'QCTF{Alb3r7_ID114mA6ic_B3rn4rd}'), ('hSN8hoHCXhytJv0ushGN', 'kN9H48ZvIe', 'QCTF{Alb3r7_vWNZ7HMdkd_B3rn4rd}'), ('SgOL8i9CZXqpMqgIZKDe', 'agDNfbTQuJ', 'QCTF{Alb3r7_g0KMO4XO8U_B3rn4rd}'), ('UxWPxnliJpNfvWktjfic', 'rLucehTXAN', 'QCTF{Alb3r7_7NClfCuKV1_B3rn4rd}'), ('OpeeWMWcz1LtRQj2WQny', 'zoGZc7empW', 'QCTF{Alb3r7_STzScBMSJ5_B3rn4rd}'), ('xFroKoVSsI4Rw74bQdip', 'F0jIjyePaL', 'QCTF{Alb3r7_JmSmvqh3D2_B3rn4rd}'), ('6SKOkk9t1bAUn9wLBmYf', 'gp3XLNMUtR', 'QCTF{Alb3r7_kxuIfuaqlX_B3rn4rd}'), ('tTOEXa2HdYM7PJcqSPAu', 'CuxQnuWWLj', 'QCTF{Alb3r7_4cT5Hv2Fq4_B3rn4rd}'), ('4kSB649Q1osnWBKTL29a', 'wX6R6tBlXv', 'QCTF{Alb3r7_LJGCEhP4fh_B3rn4rd}'), ('cwCOpxOFfOuvifophTDp', 'iRw27TjJCC', 'QCTF{Alb3r7_HXuIj2hjAG_B3rn4rd}'), ('ojlJFlcTiCFmzN1spOyU', 'N3C16D9nu4', 'QCTF{Alb3r7_om8Lc33cao_B3rn4rd}'), ('ThPx90UfWNj5aE5sBftk', 'iGDvkZzet4', 'QCTF{Alb3r7_ImvT7LTSTF_B3rn4rd}'), ('iIg1xx4XcLdSOHQFLDua', 'S2OlQpEIKF', 'QCTF{Alb3r7_STVa5w8NOi_B3rn4rd}'), ('XmkWCVZqpaUjVEz6QTUk', 'cwgCqlmZto', 'QCTF{Alb3r7_lLYHKTENtv_B3rn4rd}'), ('D8wvWE23GMPIJc0v7dms', 'VMS2B091fV', 'QCTF{Alb3r7_Oc3tauAPUb_B3rn4rd}'), ('CKj6z6liGQP5Cn3qmde7', 'axG7H4UzZ3', 'QCTF{Alb3r7_ysNXbA7Zza_B3rn4rd}'), ('mYlQLtRvsMTQStJVTIVB', 'KecA5RpeFs', 'QCTF{Alb3r7_CPHCWGkSP2_B3rn4rd}'), ('kx7tam9EkBfE3fe7iOtw', 'lr1kVrMHND', 'QCTF{Alb3r7_F2s3UVlr4g_B3rn4rd}'), ('QVnqWpoDME03plhVhdST', 'lD6mHXFT6B', 'QCTF{Alb3r7_m6Qy6SaNGo_B3rn4rd}'), ('0gyvyKL4gaeyEevLSI97', '8RPhqAWeAu', 'QCTF{Alb3r7_x3vSr1iZop_B3rn4rd}'), ('Zd1ixxsHCsjTLIqFJV8I', 'IqbOEdmuD4', 'QCTF{Alb3r7_6Mruiwn8o4_B3rn4rd}'), ('TtTu3hAud5zA1kQYZzkf', 'MMTglUJZrV', 'QCTF{Alb3r7_elvECCVko7_B3rn4rd}'), ('pSoxa6Ku3jFRDuIlKNyC', 'FF7RITxfOc', 'QCTF{Alb3r7_uVa6sHZ4mP_B3rn4rd}'), ('3nXAWR0g7FCpfwMaZuA9', '14fPHPzm9o', 'QCTF{Alb3r7_FouvmZQCwL_B3rn4rd}'), ('qL47T9WeAUFNyFq9M5qr', 'CvYVzMyb2R', 'QCTF{Alb3r7_OKnSDYN4ts_B3rn4rd}'), ('ylqRbpVLIWlFzKKXsR5E', 'q2GAbtyTdi', 'QCTF{Alb3r7_myR3hTFs0e_B3rn4rd}'), ('G5ZrZ0D5ArjDhy8Vq4aM', 'ALpIvXl77X', 'QCTF{Alb3r7_qtpvmnjrJ5_B3rn4rd}'), ('mNJ1HDawRqB5L8CqXV8q', 'rpAXwhJbVH', 'QCTF{Alb3r7_YXBFgeTM2O_B3rn4rd}'), ('D2ejHbcdg03wOAcJRifR', 'MOd06ytA8M', 'QCTF{Alb3r7_6KRAlqYKeZ_B3rn4rd}'), ('RcBGZiU3eGakyKJia1WM', 'xEfk0nHcEp', 'QCTF{Alb3r7_d7sPwhvTV4_B3rn4rd}'), ('gWGeQXVDOPle1lpEYsV8', 'DdmKtA6Yg5', 'QCTF{Alb3r7_tYTjU5Dx4D_B3rn4rd}'), ('88y7tTLLitZHY19Vb9AZ', 'otOaIDouQm', 'QCTF{Alb3r7_c1oJyYMlVj_B3rn4rd}'), ('2fXxcarCmNrWBanzf1Ru', 'R7yiDggDug', 'QCTF{Alb3r7_9XIVC1PK9A_B3rn4rd}'), ('2Xc4RotJDsKooZDPOP9R', 'CSTrKqm9x1', 'QCTF{Alb3r7_hrH7gARKtE_B3rn4rd}'), ('GTHMrJM9OMUceQss1iW5', 'Ya1Jv2VqSJ', 'QCTF{Alb3r7_EpRZaVTstj_B3rn4rd}'), ('yoIDAwFhU0hb5Y92NTZT', 'bV6yU0rif7', 'QCTF{Alb3r7_AgwR515RmY_B3rn4rd}'), ('g5N8sJBWp0gJDGrVMtWz', 'g3NV3J6BDu', 'QCTF{Alb3r7_gTMRooSWa7_B3rn4rd}'), ('p2fxLYohygIOfTVyMrAX', 'x3dBqCEjWt', 'QCTF{Alb3r7_9qvaz2bpCP_B3rn4rd}'), ('3EkCfIPIw09AKbhy6R9Q', 'CGlaaxdrFi', 'QCTF{Alb3r7_KQFY5AXAeR_B3rn4rd}'), ('zbaHd7lrQEvvJxGPoXGU', 'kYDmqMm5RB', 'QCTF{Alb3r7_hCzx76Jgv7_B3rn4rd}'), ('HcQv7nbd1Ox0yqnjNgs0', '9EQrQYmfjQ', 'QCTF{Alb3r7_p3V3hwdChg_B3rn4rd}'), ('De1owjQGeoPOY9o94bDz', 'buJgpt5mHS', 'QCTF{Alb3r7_tZ0CXrpnEu_B3rn4rd}'), ('gMykw33rD2ue8XFVQTMK', 'AV3GAvvFs1', 'QCTF{Alb3r7_z0bIIwqw4F_B3rn4rd}'), ('fi1UL3uN7UJkQP8cah0I', 'z0CD8a6Ju6', 'QCTF{Alb3r7_jow3DWHc8d_B3rn4rd}'), ('PzdynZjxvVtfSYyOsMBi', 'ZUc0tRRLAc', 'QCTF{Alb3r7_kKtlLzHNhq_B3rn4rd}'), ('6J2rCiffMwuJqIYDnF5M', '64jLktOniY', 'QCTF{Alb3r7_DTiIdpCkLl_B3rn4rd}'), ('VSgI04urCtEs43XLBOJU', 'dXsqrxIiFv', 'QCTF{Alb3r7_tne3son5LS_B3rn4rd}'), ('p1uPkNk1bU0srgKMG7Bv', 'PmTmc2zH1Q', 'QCTF{Alb3r7_Mgh6rcjZwm_B3rn4rd}'), ('jR70QOO59huqUNuAlys2', 'dVQRIw96Bi', 'QCTF{Alb3r7_J7mNFxFSIG_B3rn4rd}'), ('DUAfQRebU7lwf1qO4CAS', 'h7vvacq2Yv', 'QCTF{Alb3r7_oV5Ib40KH9_B3rn4rd}'), ('9ncMP9rSnnXokRJeNgVf', 'kDyy1WbxB9', 'QCTF{Alb3r7_ndh0R6L3Fa_B3rn4rd}'), ('UEXvQEbhq6aj17vEOGJ7', 'Gy1RBy6nG0', 'QCTF{Alb3r7_B9H1Kwor0I_B3rn4rd}'), ('cHmgSuNyKgItMEjS83o4', '6uFKDqqr5Y', 'QCTF{Alb3r7_lNy8BgNNNO_B3rn4rd}'), ('04HF7QsEAXv6aCBBus0U', '4kPKfZVXMy', 'QCTF{Alb3r7_irS3g23lfm_B3rn4rd}'), ('F7w4s7lt4atVOUUNEZEd', 'uZCCA2QYiZ', 'QCTF{Alb3r7_yGT9o4vzqj_B3rn4rd}'), ('6oXBJkIpGvbHxu553U0a', 'teNIrjIwfJ', 'QCTF{Alb3r7_u9mdmzwZT1_B3rn4rd}'), ('yna4owMiUfEYTsJJozfL', 'WfB2U2nXJL', 'QCTF{Alb3r7_CLgbCOgzCr_B3rn4rd}'), ('WnYXsUeM48gH6pupV7LD', 'VooTkAMpH3', 'QCTF{Alb3r7_y6YommNH7M_B3rn4rd}'), ('S9Xq8me6Aox7Ekh25EXu', 'QuORTd236o', 'QCTF{Alb3r7_C6zlKSBWyZ_B3rn4rd}'), ('lOyaKAIEFfgcfWX9Bw1y', 'gUIMF6zjCG', 'QCTF{Alb3r7_7x9wM0VYTQ_B3rn4rd}'), ('MRvACiqkYTakrbpgwxom', 'TuGLtwb7On', 'QCTF{Alb3r7_2FOBN18XDb_B3rn4rd}'), ('6cb2cdE6brjaP9pxjZ61', 'GZ0j9QyrnG', 'QCTF{Alb3r7_Wy3INxPyZy_B3rn4rd}'), ('ESl1AlsFIe3caMWHb07i', 'XKwL8Pf5wC', 'QCTF{Alb3r7_DbmejrUKsu_B3rn4rd}'), ('3MopDtv7P80jmZm6GERH', 'E3gTpmFsoQ', 'QCTF{Alb3r7_H1brjkU2Pw_B3rn4rd}'), ('hLSdyMVt0jH17CxKjEx2', 'tSqgN8xX08', 'QCTF{Alb3r7_trdJMPojiL_B3rn4rd}'), ('SCPaMAQA9Eh8BLREb9Qd', 'KCEMVRliJ7', 'QCTF{Alb3r7_xW03CZ6OfL_B3rn4rd}'), ('52QqOzUtRNIzFRDHwRW3', 'zDuC7fSwyU', 'QCTF{Alb3r7_pk84At9pbv_B3rn4rd}'), ('oXfBZQfacfT0BEmIEVRh', 'sCCpB6zEkW', 'QCTF{Alb3r7_Mr6fa0OMas_B3rn4rd}'), ('tbHHzDjCPCbn8lL9kI6v', 'bcwloB3uoO', 'QCTF{Alb3r7_lkn8VIp9q0_B3rn4rd}'), ('t7ayMs1fP35xDSNGGcrD', 'VbWzYyTI8S', 'QCTF{Alb3r7_f1KQdVAEgB_B3rn4rd}'), ('K3Y7m57x13eGfl5lkLqU', 'tplD2rN2VC', 'QCTF{Alb3r7_8oySPBw0LE_B3rn4rd}'), ('m3VEsX325ezUVfrkI19W', 'mK7iTWLHV3', 'QCTF{Alb3r7_Fv7JlJH4MY_B3rn4rd}'), ('ay6nEb8KwXiSIhyBC5kn', 'wiFYAoRqxl', 'QCTF{Alb3r7_MuAZd6k66h_B3rn4rd}'), ('Cm5D746Z2eJ97cllgahb', 'EEhOx5kFQ7', 'QCTF{Alb3r7_aL8H7Sac9t_B3rn4rd}'), ('CM6x78bqvmfWM45eHpms', '2p2j22Ii6e', 'QCTF{Alb3r7_oDok8lSixh_B3rn4rd}'), ('Ei2HGOmfAR0vp1SYNdUF', '23gCldEace', 'QCTF{Alb3r7_91BIgY65Q4_B3rn4rd}'), ('7YzcasqlZHOb2ypNHbjS', 'KLINijiMQB', 'QCTF{Alb3r7_BIrXC2Xmu3_B3rn4rd}'), ('IgZeXsNkWdZup8XAJorN', 'urQPjQsOYJ', 'QCTF{Alb3r7_5rxrHphCN5_B3rn4rd}'), ('RU6RDopMZcEwqsdT9E0W', 'MSz8MWy8gc', 'QCTF{Alb3r7_jFn4SIr0PE_B3rn4rd}'), ('6g4IYiZL5OtkD6fRJY0H', 'R2Gw7RwIVz', 'QCTF{Alb3r7_txGaZZRfR9_B3rn4rd}'), ('xyHvEAMRi93AEw3TkMXT', 'ROFhp9X2MU', 'QCTF{Alb3r7_jvAYFFQYok_B3rn4rd}'), ('B6UQdMKgJQuNeKEMivX2', 'G0WLC1ui5s', 'QCTF{Alb3r7_AY4P7IwD9V_B3rn4rd}'), ('KUuBlFb3kz2KIdYfJsIT', 'uoJzmPK2FA', 'QCTF{Alb3r7_K014iaV5pK_B3rn4rd}'), ('QbTys6uH8yWQ4GmIMKqU', '8fx7dx4zIl', 'QCTF{Alb3r7_SJCT7JfekB_B3rn4rd}'), ('tzoeOvlasajxAUXKNc9D', 'Yt1ybOxIAR', 'QCTF{Alb3r7_UN9K6SuSDn_B3rn4rd}'), ('0ZzsxkCWLz3Hgr938aDy', 'BoeSa3KgEz', 'QCTF{Alb3r7_wL05TswuRL_B3rn4rd}'), ('oWtIgu7IoTA8hU2aClDJ', 'mRxavCWufZ', 'QCTF{Alb3r7_csdRTlLjRj_B3rn4rd}'), ('UvZudBuKhGeu3T58b5tk', 'EBDj6kWBTE', 'QCTF{Alb3r7_LAjF80RG1a_B3rn4rd}'), ('Dod9oraD1hD94VuxBaeV', 'a7YFapdq8J', 'QCTF{Alb3r7_3HRP8C3sXF_B3rn4rd}'), ('IHD4Pqz4u6zsID6mF30V', 'T05VXo84o7', 'QCTF{Alb3r7_ZNjtIig1rt_B3rn4rd}'), ('7GvMbGlxgSU4rzELEGoK', 'OUIpRbvvn0', 'QCTF{Alb3r7_e1yobxQFwk_B3rn4rd}'), ('wv3BBxZ7P9ih2ivePvZl', 'lJ34FQDdMf', 'QCTF{Alb3r7_vmnxwg2Zxk_B3rn4rd}'), ('ByOa3EOuBNWhslrzXsdl', 'CyzOtAbWoU', 'QCTF{Alb3r7_FaZTdUimZF_B3rn4rd}'), ('UDfoXYpa3x3n0e05mC4I', 'TnUWmDyo8r', 'QCTF{Alb3r7_NED7t7wEdw_B3rn4rd}'), ('qSNjrAbnn96Y5kL3PdJa', '7fKbJB5IhZ', 'QCTF{Alb3r7_RmSyIIYBD4_B3rn4rd}'), ('hxxvz7qJNIY5klYbS6Df', 'LXXUtmCALZ', 'QCTF{Alb3r7_lJ4IpHVD0J_B3rn4rd}'), ('YOMoLVEQKYb3yvMFpS2N', '1E8wWQS5mv', 'QCTF{Alb3r7_tczjar6Rak_B3rn4rd}'), ('QiodMIdzTKdbAla5MDq2', 'Ypn3zuyQl3', 'QCTF{Alb3r7_ouGOZSKZ20_B3rn4rd}'), ('3YynU4SHNKJrcoGiIFtd', 'fod8qU39Cl', 'QCTF{Alb3r7_jRCUa1BLoQ_B3rn4rd}'), ('Tp5hykc0Az6JxVFtdPgY', 'fPyuKa5Mml', 'QCTF{Alb3r7_ycHhLqL4QO_B3rn4rd}'), ('i8GyEkKrmgjkMUn0Nlem', 'mlgcdHjA0L', 'QCTF{Alb3r7_nBS4rq6Mdu_B3rn4rd}'), ('by11hLL2fOw5Almc4in9', 'cLi0IlxFjU', 'QCTF{Alb3r7_GVMt3o5EX1_B3rn4rd}')]