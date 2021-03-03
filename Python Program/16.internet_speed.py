import speedtest
st = speedtest.Speedtest()
print(f"Download Speed: {st.download()}")
print(f"upload Speed: {st.upload()}")

