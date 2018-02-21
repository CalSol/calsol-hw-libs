n = input("number")
n = int(n)
ns = str(n)
x = (7.21+2.4*(n - 2))/2
xs = '%.2f' % (x)
xm = x - 1.27
xms = '%.2f' % (xm)
start = - (2.54 * (n - 1)) / 2
with open('layout.pretty/CST-100,' + str(n) + '.kicad_mod', 'w') as f:
    f.write('''(module CST-100,'''+ns+''' (layer F.Cu)
  (fp_text reference REF** (at 0 4.572) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value CST-100,'''+ns+''' (at 0 -5.08) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_line (start '''+xms+''' 3.175) (end '''+xms+''' 3.81) (layer F.SilkS) (width 0.15))
  (fp_line (start -'''+xms+''' 3.175) (end '''+xms+''' 3.175) (layer F.SilkS) (width 0.15))
  (fp_line (start -'''+xms+''' 3.81) (end -'''+xms+''' 3.175) (layer F.SilkS) (width 0.15))
  (fp_line (start -'''+xs+''' 3.81) (end -'''+xs+''' -4.445) (layer F.SilkS) (width 0.15))
  (fp_line (start '''+xs+''' 3.81) (end -'''+xs+''' 3.81) (layer F.SilkS) (width 0.15))
  (fp_line (start '''+xs+''' -4.445) (end '''+xs+''' 3.81) (layer F.SilkS) (width 0.15))
  (fp_line (start -'''+xs+''' -4.445) (end '''+xs+''' -4.445) (layer F.SilkS) (width 0.15))
    ''')
    for m in range(1,n+1):
        pos = start + (m - 1) * 2.54
        poss = '%0.2f' % (pos)
        f.write('''(pad '''+str(m)+''' thru_hole circle (at ''' + poss + ''' 0) (size 1.524 1.524) (drill 1.016) (layers *.Cu *.Mask))
''')
    f.write(')\n')
    f.close()
