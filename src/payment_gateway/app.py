from fastapi import FastAPI, Request
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import uvicorn
import threading
import time

app = FastAPI()

# Global variables for ROS 2 node and publisher
ros_node: Node = None
publisher: rclpy.publisher.Publisher = None

def init_ros():
    global ros_node, publisher
    if not rclpy.ok():
        rclpy.init()
    ros_node = Node('payment_gateway_node')
    publisher = ros_node.create_publisher(String, 'genie/command', 10)
    # Spin the ROS node in a background thread
    def spin_node():
        while rclpy.ok():
            rclpy.spin_once(ros_node, timeout_sec=0.1)
            time.sleep(0.01)
    spin_thread = threading.Thread(target=spin_node, daemon=True)
    spin_thread.start()

@app.on_event("startup")
async def startup_event():
    init_ros()

@app.on_event("shutdown")
async def shutdown_event():
    global ros_node
    if ros_node is not None:
        ros_node.destroy_node()
    rclpy.shutdown()

@app.post("/webhook/easypaisa")
async def easypaisa_webhook(request: Request):
    """
    Endpoint to receive transaction events from EasyPaisa.
    Placeholder for transaction verification.
    """
    # Placeholder: Verify the transaction (e.g., check signature, amount, etc.)
    # For now, we assume the transaction is valid.
    transaction_data = await request.json()
    
    # Placeholder: If transaction is verified, publish a ROS 2 message
    if True:  # Replace with actual verification
        msg = String()
        msg.data = "TRANSACTION_VERIFIED: " + str(transaction_data.get('amount', '0')) + " PKR"
        publisher.publish(msg)
        return {"status": "success", "message": "Transaction processed and ROS 2 message published"}
    else:
        return {"status": "failure", "message": "Transaction verification failed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)