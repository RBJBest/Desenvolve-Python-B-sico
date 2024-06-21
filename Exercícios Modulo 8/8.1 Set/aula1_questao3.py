turmas = [{'ações comunitárias', 'futebol', 'música', 'rugby','vôlei'},
          {'ações comunitárias', 'música', 'rugby','vôlei', 'teatro'},
          {'música', 'rugby', 'teatro', 'vôlei'},
          {'música', 'vôlei', 'rugby'},
          {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
          {'ações comunitárias', 'futebol', 'vôlei', 'rugby'},
          {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
          {'ações comunitárias', 'rugby', 'teatro'},
          {'ações comunitárias', 'rugby', 'vôlei'}
         ]
ativ_comuns = turmas[0]
for i in turmas:
    ativ_comuns = ativ_comuns.intersection(i)
print (ativ_comuns)