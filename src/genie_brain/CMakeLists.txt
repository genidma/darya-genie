cmake_minimum_required(VERSION 3.5)
package(genie_brain)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# Uncomment if you have sources to build, e.g.:
# add_executable(genie_brain_node src/genie_brain_node.cpp)
# ament_target_dependencies(genie_brain_node rclcpp rclpy std_msgs)
# install(TARGETS
#   genie_brain_node
#   DESTINATION lib/${PROJECT_NAME})
#
# If you want to install a Python package here, you need to use
# ament_python_install_package and list the package in package.xml
# under <exec_depend>ament_python</exec_depend>.

# Install package.xml
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)
install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME}/
)
install(FILES
  package.xml
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()