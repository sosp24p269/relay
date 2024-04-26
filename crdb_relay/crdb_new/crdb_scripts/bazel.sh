for ((i=100; i<250; i=i+10))
do

    cmd="cd crdb && sudo chmod +x bazelisk-linux-amd64 && sudo cp bazelisk-linux-amd64 /usr/local/bin/bazel && sudo ln -s /usr/local/bin/bazel/bazelisk-linux-amd64 /usr/bin/bazel && cd cockroach && bazel version"
    echo $cmd
    ssh -o StrictHostKeyChecking=no 10.62.0.$i $cmd
done