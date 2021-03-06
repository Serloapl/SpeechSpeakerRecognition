import proto
import tools
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from scipy.spatial import distance
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.mixture import GMM


example = np.load('example_python3.npz')['example'].item()
tidigits = np.load('tidigits_python3.npz')['tidigits']
# print(example['samples'])
# frames = proto.enframe(example['samples'], int(20000*0.02), int(20000*0.01))
# preemph = proto.preemp(frames)
# windowed = proto.windowing(preemph)
# spec = proto.powerSpectrum(windowed, 512)
# mspec = proto.logMelSpectrum(spec, 20000)
# mfcc = proto.cepstrum(mspec,13)
# lmfcc = tools.lifter(mfcc)

#
# lmfcc = proto.mfcc(example['samples'])
# print(lmfcc.shape)
aux = proto.mfcc(tidigits[4]['samples'])
plt.pcolormesh(aux.T)
plt.xlim(0, aux.shape[0])
plt.ylim(0, aux.shape[1])
plt.title(tidigits[4]['digit'])
plt.show()


aux = proto.mfcc(tidigits[8]['samples'])
plt.pcolormesh(aux.T)
plt.xlim(0, aux.shape[0])
plt.ylim(0, aux.shape[1])
plt.title(tidigits[8]['digit'])
plt.show()


matrix_tidigits = proto.correlation_mfcc(tidigits,13)
correlation_matrix = np.corrcoef(matrix_tidigits)
#
# plt.pcolormesh(correlation_matrix)
# plt.title('Correlation between Mel filterbank features')
# plt.ylim(0, len(correlation_matrix))
# plt.xlim(0, len(correlation_matrix))
# plt.show()

# x=proto.mfcc(tidigits[0]['samples'])
# y=proto.mfcc(tidigits[0]['samples'])
# result1 = (proto.dtw(x, y, distance.euclidean))
# print(result1)

# glob_mat = proto.distances_global(tidigits)
# np.save('matrix_D', glob_mat)

# D = np.load('matrix_D.npy')
# plt.pcolormesh(D)
# plt.title('Global Pairwise Distances')
# plt.ylim(0, len(D))
# plt.xlim(0, len(D))
# plt.show()
#
# dendrogram(linkage(D, method='complete'), labels = tools.tidigit2labels(tidigits))
# plt.title('Hierarchical Clustering on Global Distances')
# plt.show()
#

gmm_matrix1 = proto.mfcc(tidigits[16]['samples'])
gmm_matrix2 = proto.mfcc(tidigits[17]['samples'])
gmm_matrix3 = proto.mfcc(tidigits[38]['samples'])
gmm_matrix4 = proto.mfcc(tidigits[39]['samples'])
# Utterances for word seven

clf = GMM(n_components=4, random_state=400)
clf.fit(matrix_tidigits)

labels1 = clf.predict(gmm_matrix1)
plt.plot(labels1)
labels2 = clf.predict(gmm_matrix2)
plt.plot(labels2)
labels3_prob = clf.predict_proba(gmm_matrix3)
labels3 = clf.predict(gmm_matrix3)
# plt.pcolormesh(labels3_prob.T)
# plt.xlim(0, labels3_prob.shape[0])
# plt.ylim(0, labels3_prob.shape[1]) // Para plotear con mapa de colores
plt.plot(labels3, 'k')
# labels4_prob = clf.predict_proba(gmm_matrix4)
labels4 = clf.predict(gmm_matrix4)
# plt.pcolormesh(labels4_prob.T)
plt.plot(labels4,'m')
plt.title('Man and woman utterances for word \'seven\'')
plt.show()



# plt.pcolormesh(glob_mat)
# plt.show()

# lmfcc_tidigits = proto.mfcc(tidigits[7]['samples'])
# print(tidigits[3]['digit'])
#
# plt.pcolormesh(lmfcc_tidigits.T)
# plt.show()
#
# plt.pcolormesh(lmfcc)
# plt.show()


