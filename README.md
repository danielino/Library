OS Library


example:

Linux:
	import Linux
	
	refer to the Doc directory for documentation of module
	

	available Package:
	
		Device:
			Linux.Device
			Linux.Device.disk			<-- disk operation
			Linux.Device.fc				<-- fibre channel hba operation
			Linux.Device.network		<-- manage network cards
				@network module
				Linux.Device.network.all_interfaces()
				Linux.Device.network.get_iface_info(iface_name)
		
		
		Kernel:
			
			Linux.Kernel.version		<-- version of current kernel
			
			Linux.Kernel.proc
				@proc module			
				Linux.Kernel.proc.get_pid_status()
				Linux.Kernel.proc.parse_status_file()
				Linux.Kernel.proc.get_pid_open_fd()
		
		
		Release 
			Linux.Release
			
			Debian:
				Linux.Release.Debian
				
			Gentoo:
				Linux.Release.Gentoo
				
			RedHat:
				Linux.Release.RedHat
				
				Linux.Release.RedHat.RHN 	<-- manage RHN subscription and repository
					Linux.Release.RedHat.RHN.is_registered()
					Linux.Release.RedHat.RHN.register(rhn_username, rhn_password, system_proxy="")
					
				Linux.Release.RedHat.package
					Linux.Release.RedHat.package.is_installed(pkg_name)
					Linux.Release.RedHat.package.return_package_installed()
				
				
			Ubuntu:
				Linux.Release.Ubuntu
				
				
		Security		
			Iptables
				Linux.Security.iptables
				Linux.Security.iptables.chain
				Linux.Security.iptables.rules
			
			SELinux
				Linux.Security.SELinux
				
				
		Storage
			Linux.Storage
			Linux.Storage.Local
			Linux.Storage.Lun
			Linux.Storage.MultiPath
			
			
			
	available Module:
	
		Linux.console
		#console Module 
			# console function
			# available function
				Linux.console.run_command(command):
				Linux.console.colored(text,
				Linux.console.binary_exists(binary):	
					
		
		Linux.group
		# group Module 
			# manage group
			# available function
				Linux.group.group_exists(groupname):
				Linux.group.find_by_gid(gid):
				Linux.group.find_by_name(groupname):
				Linux.group.create(groupname,
				Linux.group.delete(groupname):	
					
			
		Linux.IO
		# IO Module
			# file operation
			#available function
				Linux.IO.file_exists(fileName):
				Linux.IO.open_file(fileName,
				Linux.IO.write_file(fileName,
				Linux.IO.read_file(filePointer):
				
			
		Linux.process
		# process Module 
			# get process info
			# available function
				Linux.process.get_pid(p_name)
				Linux.process.pgrep_get_status(p_name)
				Linux.process.get_pid_fd_open(p_name)
			
			
		Linux.service
		# service Module 
			# provide stop, start, status, restart and reload method for service ( use /etc/init.d/service_name )
			# available function
				Linux.service.service_exists(service_name)
				Linux.service.stop(service_name)
				Linux.service.start(service_name)
				Linux.service.restart(service_name)
				Linux.service.status(service_name)
				Linux.service.reload(service_name)
		
		
		Linux.user
		# user Module 
			# manage user
			# available function
				Linux.user.user_exists(username):
				Linux.user.get_all_user():
				Linux.user.get_user_info(username):
				Linux.user.find_by_uid(uid):
				Linux.user.create(username,
				Linux.user.delete(username):
				Linux.user.change_password(username, password)
				
			
		
