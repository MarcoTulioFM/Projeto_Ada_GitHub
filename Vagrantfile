Vagrant.configure("2") do |config|
  (1..2).each do |i|
      config.vm.define "node#{i}" do |machine|
          machine.vm.box = "bento/ubuntu-22.04"
          machine.vm.provider "virtualbox" do |vb|
              vb.cpus = 2
              vb.memory = 2048
              vb.name = "node#{i}"
          end
          machine.vm.network "public_network" , bridge: "Realtek PCIe GbE Family Controller"
          machine.vm.provision "shell", path: "script.sh"
          machine.vm.provision "file", source: "Projeto_Ada_Github", destination: "~/Projeto_Ada_Github"
      end
  end
end
