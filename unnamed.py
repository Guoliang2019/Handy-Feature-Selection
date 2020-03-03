def transform1Darray(arr,win_len,overlap):
  n_obs = (arr.size - overlap)//(win_len - overlap)
  arr = arr[-(n_obs*(win_len-overlap)+overlap):]
  output = as_strided(arr,(arr.size-win_len+1,win_len),arr.strides*2)
  idx = np.arange(0,output.shape[0],win_len-overlap)
  return output[idx]
